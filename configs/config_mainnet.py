chain_network = "mainnet"

# DAO
lido_dao_kernel = "0xb8FFC3Cd6e7Cf5a098A1c92F48009765B24088Dc"
ldo_token_address = "0x5A98FcBEA516Cf06857215779Fd812CA3beF1B32"
lido_dao_kernel_implementation = "0x2b33CF282f867A7FF693A66e11B0FcC5552e4425"

# Standard (or forked) Aragon apps
lido_dao_acl_address = "0x9895F0F17cc1d1891b6f18ee0b483B6f221b37Bb"
lido_dao_agent_address = "0x3e40D73EB977Dc6a537aF587D48316feE66E9C8c"
lido_dao_finance_address = "0xB9E5CBB9CA5b0d659238807E84D0176930753d86"
lido_dao_voting_address = "0x2e59A20f205bB85a89C53f1936454680651E618e"
lido_dao_token_manager_address = "0xf73a1260d222f447210581DDf212D915c09a3249"
lido_dao_acl_implementation_address = "0x9f3b9198911054B122fDb865f8A5Ac516201c339"
lido_dao_voting_implementation_address = "0x72fb5253AD16307B9E773d2A78CaC58E309d5Ba4"

# Our custom Aragon apps
lido_dao_steth_address = "0xae7ab96520DE3A18E5e111B5EaAb095312D7fE84"
lido_dao_legacy_oracle = "0x442af784A788A5bd6F42A01Ebe9F287a871243fb"
lido_dao_node_operators_registry = "0x55032650b14df07b85bF18A3a3eC8E0Af2e028d5"
lido_dao_steth_implementation_address_v1 = "0x47EbaB13B806773ec2A2d16873e2dF770D130b50"
lido_dao_legacy_oracle_implementation_v1 = "0x1430194905301504e8830ce4B0b0df7187E84AbD"
lido_dao_node_operators_registry_implementation_v1 = "0x5d39ABaa161e622B99D45616afC8B837E9F19a25"

# Aragon APM Repos
lido_dao_voting_repo = "0x4Ee3118E3858E8D7164A634825BfE0F73d99C792"
lido_dao_lido_repo = "0xF5Dc67E54FC96F993CD06073f71ca732C1E654B1"
lido_dao_node_operators_registry_repo = "0x0D97E876ad14DB2b183CFeEB8aa1A5C788eB1831"
lido_dao_legacy_oracle_repo = "0xF9339DE629973c60c4d2b76749c81E6F40960E3A"
## lido_dao_aragon_repo_implementation is common for Lido, NodeOperatorsRegistry, Oracle aragon apps
lido_dao_aragon_repo_implementation = "0xa8A358E9bbB9fF60D4B89CBE5b2FE88f98b51B9D"

# Other Aragon contracts
## For lido_dao_evm_script_registry see Aragon Agent 0x853cc0D5917f49B57B8e9F89e491F5E18919093A
lido_dao_evm_script_registry = "0x853cc0D5917f49B57B8e9F89e491F5E18919093A"
## See getEVMScriptExecutor(0x00000001) of any Aragon App or callsScript of lido_easytrack_evmscriptexecutor
lido_dao_calls_script = "0x5cEb19e1890f677c3676d5ecDF7c501eBA01A054"

# Other (non-aragon) protocol contracts
wsteth_token_address = "0x7f39C581F595B53c5cb19bD0b3f8dA6c935E2Ca0"
lido_dao_execution_layer_rewards_vault = "0x388C818CA8B9251b393131C08a736A67ccB19297"
lido_dao_deposit_security_module_address_v1 = "0x710B3303fB508a84F10793c1106e32bE873C24cd"
lido_dao_withdrawal_vault = "0xB9D7934878B5FB9610B3fE8A5e441e8fad7E293f"

# EasyTracks
lido_easytrack = "0xF0211b7660680B49De1A7E9f25C65660F0a13Fea"
lido_easytrack_evmscriptexecutor = "0xFE5986E06210aC1eCC1aDCafc0cc7f8D63B3F977"
lido_easytrack_increase_nop_staking_limit_factory = "0xFeBd8FAC16De88206d4b18764e826AF38546AfE0"

# Multisigs
finance_multisig_address = "0x48F300bD3C52c7dA6aAbDE4B683dEB27d38B9ABb"

# Other
lido_insurance_fund_address = "0x8B3f33234ABD88493c0Cd28De33D583B70beDe35"
lido_relay_allowed_list = "0xF95f069F9AD107938F6ba802a3da87892298610E"
curve_rewards_manager_address = "0x753D5167C31fBEB5b49624314d74A957Eb271709"
balancer_rewards_manager = "0x1dD909cDdF3dbe61aC08112dC0Fdf2Ab949f79D8"

# Auxiliary addresses
ldo_holder_address_for_tests = "0x9bb75183646e2a0dc855498bacd72b769ae6ced3"
ldo_vote_executors_for_tests = [
    "0x3e40d73eb977dc6a537af587d48316fee66e9c8c",
    "0xb8d83908aab38a159f3da47a59d84db8e1838712",
    "0xa2dfc431297aee387c05beef507e5335e684fbcd",
]
# General network addresses
dai_token_address = "0x6b175474e89094c44da98b954eedeac495271d0f"
weth_token_address = "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"


#
# Shapella upgrade entries
# Grouped the same as in docs
#

# LidoLocator
lido_dao_lido_locator = "0xC1d0b3DE6792Bf6b4b37EccdcC24e45978Cfd2Eb"
lido_dao_lido_locator_implementation = "0x1D920cc5bACf7eE506a271a5259f2417CaDeCE1d"

lido_dao_template_address = "0xa818fF9EC93122Bf9401ab4340C42De638CD600a"

# Misc upgrade addresses
dummy_implementation_address = "0x6F6541C2203196fEeDd14CD2C09550dA1CbEDa31"
initial_dead_token_holder = "0x000000000000000000000000000000000000dead"
deployer_eoa_locator = "0x2A78076BF797dAC2D25c9568F79b61aFE565B88C"
deployer_eoa = "0x8Ea83AD72396f1E0cD2f8E72b1461db8Eb6aF7B5"

# 0x01...withdrawal_vault or Lido.getWithdrawalCredentials()
WITHDRAWAL_CREDENTIALS = "0x010000000000000000000000b9d7934878b5fb9610b3fe8a5e441e8fad7e293f"

# Lido
lido_dao_steth_implementation_address = "0x17144556fd3424EDC8Fc8A4C940B2D04936d17eb"
# see Lido's proxy appId()
LIDO_APP_ID = "0x3ca7c3e38968823ccb4c78ea688df41356f182ae1d159e4ee608d30d68cef320"
LIDO_MAX_STAKE_LIMIT_ETH = 150_000

# LegacyOracle (former LidoOracle)
## address is lido_dao_legacy_oracle
lido_dao_legacy_oracle_implementation = "0xa29b819654cE6224A222bb5f586920105E2D7E0E"
## see LidoOracle's proxy appId()
ORACLE_APP_ID = "0x8b47ba2a8454ec799cd91646e7ec47168e91fd139b23f017455f3e5898aaba93"

# NodeOperatorsRegistry akd Curated Staking Module
lido_dao_node_operators_registry_implementation = "0x8538930c385C0438A357d2c25CB3eAD95Ab6D8ed"
# see NodeOperatorsRegistry's proxy appId()
NODE_OPERATORS_REGISTRY_APP_ID = "0x7071f283424072341f856ac9e947e7ec0eb68719f757a7e785979b6b8717579d"
STUCK_PENALTY_DELAY = 432000
STAKING_MODULE_NOR_TARGET_SHARE_BP = 10000
STAKING_MODULE_NOR_MODULE_FEE = 500
STAKING_MODULE_NOR_TREASURY_FEE = 500
CURATED_NODE_OPERATORS_COUNT = 30
CURATED_NODE_OPERATORS_ACTIVE_COUNT = 30
STAKING_MODULE_NOR_ID = 1
STAKING_MODULE_NOR_NAME = "curated-onchain-v1"
STAKING_MODULE_NOR_TYPE = (
    # bytes32("curated-onchain-v1")
    "0x637572617465642d6f6e636861696e2d76310000000000000000000000000000"
)

# OracleDaemonConfig
oracle_daemon_config = "0xbf05A929c3D7885a6aeAd833a992dA6E5ac23b09"
NORMALIZED_CL_REWARD_PER_EPOCH = 64
NORMALIZED_CL_REWARD_MISTAKE_RATE_BP = 1000  # 10%
REBASE_CHECK_NEAREST_EPOCH_DISTANCE = 1
REBASE_CHECK_DISTANT_EPOCH_DISTANCE = 23  # 10% of AO 225 epochs frame
VALIDATOR_DELAYED_TIMEOUT_IN_SLOTS = 7200  # 1 day
VALIDATOR_DELINQUENT_TIMEOUT_IN_SLOTS = 28800  # 4 days
NODE_OPERATOR_NETWORK_PENETRATION_THRESHOLD_BP = 100  # 1%
PREDICTION_DURATION_IN_SLOTS = 50400
FINALIZATION_MAX_NEGATIVE_REBASE_EPOCH_SHIFT = 1350  # 6 days

# OracleReportSanityChecker
lido_dao_oracle_report_sanity_checker = "0x9305c1Dbfe22c12c66339184C0025d7006f0f1cC"
CHURN_VALIDATORS_PER_DAY_LIMIT = 20000
ONE_OFF_CL_BALANCE_DECREASE_BP_LIMIT = 500  # 5%
ANNUAL_BALANCE_INCREASE_BP_LIMIT = 1000  # 10%
SIMULATED_SHARE_RATE_DEVIATION_BP_LIMIT = 50  # 0.5%
MAX_VALIDATOR_EXIT_REQUESTS_PER_REPORT = 600
MAX_ACCOUNTING_EXTRA_DATA_LIST_ITEMS_COUNT = 2
MAX_NODE_OPERATORS_PER_EXTRA_DATA_ITEM_COUNT = 100
REQUEST_TIMESTAMP_MARGIN = 7680  # 2 hours rounded to epoch length
MAX_POSITIVE_TOKEN_REBASE = 750000

# Burner
lido_dao_burner = "0xD15a672319Cf0352560eE76d9e89eAB0889046D3"
TOTAL_NON_COVER_SHARES_BURNT = 32145684728326685744
TOTAL_COVER_SHARES_BURNT = 0

# DepositSecurityModule
lido_dao_deposit_security_module_address = "0xC77F8768774E1c9244BEed705C4354f2113CFc09"
DSM_MAX_DEPOSITS_PER_BLOCK = 150
DSM_MIN_DEPOSIT_BLOCK_DISTANCE = 25
DSM_PAUSE_INTENT_VALIDITY_PERIOD_BLOCKS = 6646
## Migrated from lido_dao_deposit_security_module_address_v1
deposit_security_module_guardians = [
    "0x5fd0dDbC3351d009eb3f88DE7Cd081a614C519F1",
    "0x7912Fa976BcDe9c2cf728e213e892AD7588E6AaF",
    "0x14D5d5B71E048d2D75a39FfC5B407e3a3AB6F314",
    "0xf82D88217C249297C6037BA77CE34b3d8a90ab43",
    "0xa56b128Ea2Ea237052b0fA2a96a387C0E43157d8",
    "0xd4EF84b638B334699bcf5AF4B0410B8CCD71943f",
]
DSM_GUARDIAN_QUORUM = 4

# AccountingOracle
# and its corresponding HashConsensus
lido_dao_accounting_oracle = "0x852deD011285fe67063a08005c71a85690503Cee"
lido_dao_accounting_oracle_implementation = "0xF3c5E0A67f32CF1dc07a8817590efa102079a1aF"
lido_dao_hash_consensus_for_accounting_oracle = "0xD624B08C83bAECF0807Dd2c6880C3154a5F0B288"
ACCOUNTING_ORACLE_EPOCHS_PER_FRAME = 225
ACCOUNTING_ORACLE_CONSENSUS_VERSION = 1
ACCOUNTING_ORACLE_FAST_LANE_LENGTH_SLOTS = 100

# ValidatorsExitBusOracle
lido_dao_validators_exit_bus_oracle = "0x0De4Ea0184c2ad0BacA7183356Aea5B8d5Bf5c6e"
lido_dao_validators_exit_bus_oracle_implementation = "0xA89Ea51FddE660f67d1850e03C9c9862d33Bc42c"
lido_dao_hash_consensus_for_validators_exit_bus_oracle = "0x7FaDB6358950c5fAA66Cb5EB8eE5147De3df355a"
VALIDATORS_EXIT_BUS_ORACLE_EPOCHS_PER_FRAME = 75
VALIDATORS_EXIT_BUS_CONSENSUS_VERSION = 1
VALIDATORS_EXIT_BUS_FAST_LANE_LENGTH_SLOTS = 100

# Ethereum Chain parameters
CHAIN_SLOTS_PER_EPOCH = 32
CHAIN_SECONDS_PER_SLOT = 12
CHAIN_GENESIS_TIME = 1606824023

# AccountingOracle and ValidatorsExitBusOracle
## Migrated from LidoOracle (LegacyOracle)
ORACLE_QUORUM = 5
oracle_committee = (
    "0x140Bd8FbDc884f48dA7cb1c09bE8A2fAdfea776E",
    "0x1d0813bf088BE3047d827D98524fBf779Bc25F00",
    "0x404335BcE530400a5814375E7Ec1FB55fAff3eA2",
    "0x946D3b081ed19173dC83Cd974fC69e1e760B7d78",
    "0x007DE4a5F7bc37E2F26c0cb2E8A95006EE9B89b5",
    "0xEC4BfbAF681eb505B94E4a7849877DC6c600Ca3A",
    "0x61c91ECd902EB56e314bB2D5c5C07785444Ea1c8",
    "0x1Ca0fEC59b86F549e1F1184d97cb47794C8Af58d",
    "0xA7410857ABbf75043d61ea54e07D57A6EB6EF186",
)

# WithdrawalQueueERC721
lido_dao_withdrawal_queue = "0x889edC2eDab5f40e902b864aD4d7AdE8E412F9B1"
lido_dao_withdrawal_queue_implementation = "0xE42C659Dc09109566720EA8b2De186c2Be7D94D9"
WITHDRAWAL_QUEUE_ERC721_NAME = "Lido: stETH Withdrawal NFT"
WITHDRAWAL_QUEUE_ERC721_SYMBOL = "unstETH"
WITHDRAWAL_QUEUE_ERC721_BASE_URI = ""

# WithdrawalsVault
lido_dao_withdrawal_vault_implementation_v1 = "0xe681faB8851484B57F32143FD78548f25fD59980"
lido_dao_withdrawal_vault_implementation = "0xCC52f17756C04bBa7E377716d7062fC36D7f69Fd"

# EIP712StETH
lido_dao_eip712_steth = "0x8F73e4C2A6D852bb4ab2A45E6a9CF5715b3228B7"

# StakingRouter
lido_dao_staking_router = "0xFdDf38947aFB03C621C71b06C9C70bce73f12999"
lido_dao_staking_router_implementation = "0xD8784e748f59Ba711fB5643191Ec3fAdD50Fb6df"
deposit_contract = "0x00000000219ab540356cBB839Cbe05303d7705Fa"
STAKING_MODULES_FEE_E4 = STAKING_MODULE_NOR_MODULE_FEE
STAKING_MODULES_TREASURY_FEE_E4 = STAKING_MODULE_NOR_TREASURY_FEE
STAKING_MODULES_FEE_E20 = 5 * 10**18
STAKING_MODULES_TREASURY_FEE_E20 = 5 * 10**18

# GateSeal
gate_seal_factory_address = "0x6C82877cAC5a7A739f16Ca0A89c0A328B8764A24"
gate_seal_address = "0x1aD5cb2955940F998081c1eF5f5F00875431aA90"
GATE_SEAL_PAUSE_DURATION_SECONDS = 518400  # 6 days
GATE_SEAL_EXPIRY_TIMESTAMP = 1714521600  # 2024-05-01 00:00GMT
gate_seal_committee_address = "0x8772E3a2D86B9347A2688f9bc1808A6d8917760C"

# Aragon Permissions
ACL_DEPLOY_BLOCK_NUMBER = 11473216

# Obsolete
lido_dao_self_owned_steth_burner = "0xB280E33812c0B09353180e92e27b8AD399B07f26"
