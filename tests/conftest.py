import os
import json
from typing import Optional, List

import pytest

from brownie import chain, interface
from brownie.network import state
from brownie.network.contract import Contract

from utils.evm_script import EMPTY_CALLSCRIPT

from utils.config import contracts, network_name

from utils.config import (
    ldo_holder_address_for_tests,
    ldo_vote_executors_for_tests,
    contract_address_mapping,
)
from utils.txs.deploy import deploy_from_prepared_tx

ENV_OMNIBUS_BYPASS_EVENTS_DECODING = "OMNIBUS_BYPASS_EVENTS_DECODING"
ENV_PARSE_EVENTS_FROM_LOCAL_ABI = "PARSE_EVENTS_FROM_LOCAL_ABI"
ENV_OMNIBUS_VOTE_IDS = "OMNIBUS_VOTE_IDS"


@pytest.fixture(scope="function", autouse=True)
def shared_setup(fn_isolation):
    pass


@pytest.fixture(scope="module")
def ldo_holder(accounts):
    return accounts.at(ldo_holder_address_for_tests, force=True)


@pytest.fixture(scope="module")
def unknown_person(accounts):
    return accounts.at("0x98ec059dc3adfbdd63429454aeb0c990fba4a128", force=True)


@pytest.fixture(scope="module")
def eth_whale(accounts):
    if network_name() in ("goerli", "goerli-fork"):
        return accounts.at("0xC48E23C5F6e1eA0BaEf6530734edC3968f79Af2e", force=True)
    else:
        return accounts.at("0x00000000219ab540356cBB839Cbe05303d7705Fa", force=True)


class Helpers:
    @staticmethod
    def filter_events_from(addr, events):
        return list(filter(lambda evt: evt.address == addr, events))

    @staticmethod
    def assert_single_event_named(evt_name, tx, evt_keys_dict):
        receiver_events = Helpers.filter_events_from(tx.receiver, tx.events[evt_name])
        assert len(receiver_events) == 1
        assert dict(receiver_events[0]) == evt_keys_dict

    @staticmethod
    def execute_votes_sequential(accounts, vote_ids, dao_voting, topup="0.1 ether", skip_time=3 * 60 * 60 * 24):
        OBJECTION_PHASE_ID = 1
        for vote_id in vote_ids:
            print(f"Vote #{vote_id}")
            if dao_voting.canVote(vote_id, ldo_vote_executors_for_tests[0]) and (
                dao_voting.getVotePhase(vote_id) != OBJECTION_PHASE_ID
            ):
                for holder_addr in ldo_vote_executors_for_tests:
                    print("voting from acct:", holder_addr)
                    if accounts.at(holder_addr, force=True).balance() < topup:
                        accounts[0].transfer(holder_addr, topup)
                    account = accounts.at(holder_addr, force=True)
                    dao_voting.vote(vote_id, True, False, {"from": account})

        # wait for the vote to end
        chain.sleep(skip_time)
        chain.mine()

        for vote_id in vote_ids:
            assert dao_voting.canExecute(vote_id)

        # try to instantiate script executor
        # to deal with events parsing properly
        # on fresh brownie setup cases (mostly for CI)
        executor_addr = dao_voting.getEVMScriptExecutor(EMPTY_CALLSCRIPT)
        try:
            _ = interface.CallsScript(executor_addr)
        except:
            print("Unable to instantiate CallsScript")
            print("Trying to proceed further as is...")

        execution_transactions = []
        for vote_id in vote_ids:
            tx = dao_voting.executeVote(vote_id, {"from": accounts[0]})
            print(f"vote #{vote_id} executed")
            execution_transactions.append(tx)
        return execution_transactions

    @staticmethod
    def is_executed(vote_id, dao_voting):
        vote_status = dao_voting.getVote(vote_id)
        return vote_status[1]


@pytest.fixture(scope="session")
def helpers():
    return Helpers


@pytest.fixture(scope="session")
def vote_ids_from_env() -> List[int]:
    if os.getenv(ENV_OMNIBUS_VOTE_IDS):
        try:
            vote_ids_str = os.getenv(ENV_OMNIBUS_VOTE_IDS)
            vote_ids = [int(s) for s in vote_ids_str.split(",")]
            print(f"OMNIBUS_VOTE_IDS env var is set, using existing votes {vote_ids}")
            return vote_ids
        except:
            pass

    return []


@pytest.fixture(scope="module")
def bypass_events_decoding() -> bool:
    if os.getenv(ENV_OMNIBUS_BYPASS_EVENTS_DECODING):
        print(f"Warning: {ENV_OMNIBUS_BYPASS_EVENTS_DECODING} env var is set, events decoding disabled")
        return True

    return False


@pytest.fixture(scope="module")
def autodeploy_contract(accounts):
    address = deploy_from_prepared_tx(accounts[0], "./utils/txs/tx-deploy-voting_for_upgrade.json")


@pytest.fixture(scope="session")
def stranger(accounts):
    return accounts[9]


@pytest.fixture(scope="session", autouse=True)
def parse_events_from_local_abi():
    if os.getenv(ENV_OMNIBUS_BYPASS_EVENTS_DECODING):
        return

    if os.getenv(ENV_PARSE_EVENTS_FROM_LOCAL_ABI):
        interface_path_template = "interfaces/{}.json"
        for contract_name, addresses in contract_address_mapping.items():
            for addr in addresses:
                with open(interface_path_template.format(contract_name)) as fp:
                    abi = json.load(fp)
                contract = Contract.from_abi(contract_name, addr, abi)
                state._add_contract(contract)
