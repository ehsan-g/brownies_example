from brownie import accounts, config, SimpleStorage
import os


def deploy_simple_storage():
    # 1- for local blockchain
    account = accounts[0]

    # 2- metamask - rinkbey
    # command: brownie accounts new <customAccountName>
    # account = accounts.load("customAccount")

    # 3- env variable with yaml
    # account = accounts.add(os.getenv("PRIVATE_KEY"))
    # account = accounts.add(config["wallets"]["from_key"])

    simple_storage = SimpleStorage.deploy({"from": account})


def main():
    deploy_simple_storage()
