from brownie import network, accounts, config

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache", "mainnet-fork"]

def get_account(index=None, id=None):
    if index:
        # 'accounts' allows you to access all your local accounts.
        # Each individual account is represented by an Account object that can
        # perform actions such as querying a balance or sending ETH.
        return accounts[index]
    if id:
        # load previously created brownie account on the system
        # these accounts can be found using the command `brownie accounts list`
        return accounts.load(id)
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
    ):
        return accounts[0]
    
    # if on real network (only works for the Rinkeby testnet for now), add the account
    # associated with the private key
    return accounts.add(config["wallets"]["from_key"])