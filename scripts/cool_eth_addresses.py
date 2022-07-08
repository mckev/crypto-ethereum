"""
Generate Ethereum wallets which have predefined suffix.
"""
from classes.bip39 import Bip39
from classes.ethereum import Ethereum

while True:
    mnemonics: list[str] = Bip39.generate_random_mnemonics_256()
    wallet = Ethereum.generate_wallet(mnemonics)
    if wallet['ethereum_address'].lower().endswith('feed'):
        print(f'{mnemonics}: {wallet["ethereum_address"]}')
