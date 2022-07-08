import unittest

from classes.ethereum import Ethereum


class TestEthereum(unittest.TestCase):

    def test_keccak256(self):
        # Ref: https://github.com/ethereum/eth-hash/blob/master/eth_hash/main.py
        hashed: bytes = Ethereum.keccak256(b'')
        self.assertEqual(hashed,
                         b"\xc5\xd2F\x01\x86\xf7#<\x92~}\xb2\xdc\xc7\x03\xc0\xe5\x00\xb6S\xca\x82';\x7b\xfa\xd8\x04]\x85\xa4p")
        self.assertEqual(hashed.hex(), 'c5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470')

    def test_checksum_ethereum_address(self):
        # Ref: https://github.com/ethereum/EIPs/blob/master/EIPS/eip-55.md
        ethereum_address_in_bytes: bytes = bytes.fromhex('5aaeb6053f3e94c9b9a09f33669435e7ef1beaed')
        ethereum_address: str = Ethereum.checksum_ethereum_address(ethereum_address_in_bytes)
        self.assertEqual(ethereum_address, '0x5aAeb6053F3E94C9b9A09f33669435E7Ef1BeAed')

    def test_generate_wallet(self):
        # Ref: https://iancoleman.io/bip39/  >  Coin: ETH - Ethereum
        mnemonics: list[str] = ['charge', 'rotate', 'december', 'sense', 'wood', 'struggle', 'cradle', 'retire', 'file',
                                'umbrella', 'render', 'route', 'hurry', 'miracle', 'maximum', 'unfair', 'people',
                                'twelve', 'hazard', 'fog', 'dog', 'guard', 'quote', 'nominee']
        wallet = Ethereum.generate_wallet(mnemonics)
        self.assertEqual(wallet, {
            'private_key': '62ed727f92a2b3656ea1dd75a1c6294c8ab67543f2b858f13c3b59a834d3ddb6',
            'public_key': '028fa063e738cd4ccc8a9b3ea91cbc433f0e009508e818e56c0f3ed7ed3d80cc5f',
            'ethereum_address': '0xd4b4F504353Cc74aD03608B0e5E3ef3437552368'
        })
