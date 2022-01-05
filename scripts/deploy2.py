from brownie import accounts, config, SimpleStorage, network


def deploy_simple_storage():
    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)

# development and rinkeby infura
def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        # brownie run scripts/deploy2.py --network rinkeby
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()