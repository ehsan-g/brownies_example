1. Install Brownie

```bash
python3 -m pip install --user pipx
python3 -m pipx ensurepath
# restart your terminal
pipx install eth-brownie
```

Or, if that doesn't work, via pip

```bash
pip install eth-brownie
```

2. Deploy to a testnet

Add your `WEB3_INFURA_PROJECT_ID` from [Infura](https://infura.io/) to your `.env` and run

```bash
source .env
```

To set your environment variable. You can check you've done it correctly with:

```bash
echo $WEB3_INFURA_PROJECT_ID
```

Then run:

```
brownie run scripts/deploy.py --network rinkeby
```

## Add network (ganache, avalanche, ...)

```bash
brownie networks list
```

```bash
brownie networks add Ethereum my-ganache-local host=http://127.0.0.1:7545 chainid=1337
```

Local mainnet fork:

```bash
brownie networks add development mainnet-fork-dev2 cmd=ganache-cli host=http://127.0.0.1 fork=https://eth-rinkeby.alchemyapi.io/v2/y9iyRjvbK6Q5SrX2mx96Ch9pv-7rcfOn accounts=10 mnemonic=brownie port=8545
```

## Add account (metamask / rinkeby)

```bash
brownie accounts new <account name>
```
