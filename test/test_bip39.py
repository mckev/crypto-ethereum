import unittest

from classes.bip39 import Bip39


class TestBip39(unittest.TestCase):

    def test_mnemonics_to_seed_01(self):
        # Ref: https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki#Test_vectors
        mnemonics: list[str] = ['abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'abandon',
                                'abandon', 'abandon', 'abandon', 'about']
        seed: bytes = Bip39.mnemonics_to_seed(mnemonics, passphrase='TREZOR')
        self.assertEqual(seed.hex(),
                         'c55257c360c07c72029aebc1b53c05ed0362ada38ead3e3e9efa3708e53495531f09a6987599d18264c1e1c92f2cf141630c7a3c4ab7c81b2f001698e7463b04')

    def test_mnemonics_to_seed_02(self):
        # Ref: https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki#Test_vectors
        mnemonics: list[str] = ['abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'abandon',
                                'abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'abandon',
                                'abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'art']
        seed: bytes = Bip39.mnemonics_to_seed(mnemonics, passphrase='TREZOR')
        self.assertEqual(seed.hex(),
                         'bda85446c68413707090a52022edd26a1c9462295029f2e60cd7c4f2bbd3097170af7a4d73245cafa9c3cca8d561a7c3de6f5d4a10be8ed2a5e608d68f92fcc8')

    def test_mnemonics_to_seed_03(self):
        # Ref: https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki#Test_vectors
        mnemonics: list[str] = ['vessel', 'ladder', 'alter', 'error', 'federal', 'sibling', 'chat', 'ability', 'sun',
                                'glass', 'valve', 'picture']
        seed: bytes = Bip39.mnemonics_to_seed(mnemonics, passphrase='TREZOR')
        self.assertEqual(seed.hex(),
                         '2aaa9242daafcee6aa9d7269f17d4efe271e1b9a529178d7dc139cd18747090bf9d60295d0ce74309a78852a9caadf0af48aae1c6253839624076224374bc63f')

    def test_mnemonics_to_seed_04(self):
        # Ref: https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki#Test_vectors
        mnemonics: list[str] = ['void', 'come', 'effort', 'suffer', 'camp', 'survey', 'warrior', 'heavy', 'shoot',
                                'primary', 'clutch', 'crush', 'open', 'amazing', 'screen', 'patrol', 'group', 'space',
                                'point', 'ten', 'exist', 'slush', 'involve', 'unfold']
        seed: bytes = Bip39.mnemonics_to_seed(mnemonics, passphrase='TREZOR')
        self.assertEqual(seed.hex(),
                         '01f5bced59dec48e362f2c45b5de68b9fd6c92c6634f44d6d40aab69056506f0e35524a518034ddc1192e1dacd32c1ed3eaa3c3b131c88ed8e7e54c49a5d0998')
