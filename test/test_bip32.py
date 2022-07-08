import unittest

from classes.bip32 import Bip32


class TestBip32(unittest.TestCase):

    def test_from_seed_01(self):
        seed: bytes = bytes.fromhex(
            'bda85446c68413707090a52022edd26a1c9462295029f2e60cd7c4f2bbd3097170af7a4d73245cafa9c3cca8d561a7c3de6f5d4a10be8ed2a5e608d68f92fcc8')
        chain_code, private_key = Bip32.from_seed(seed)
        self.assertEqual(list(chain_code),
                         [97, 204, 178, 187, 231, 210, 164, 252, 205, 95, 65, 142, 233, 49, 219, 124, 186, 201, 161, 83,
                          236, 67, 176, 174, 55, 89, 255, 153, 30, 77, 35, 209])
        self.assertEqual(list(private_key),
                         [200, 180, 7, 60, 207, 204, 99, 71, 92, 61, 82, 2, 198, 89, 68, 132, 238, 78, 119, 184, 103,
                          205, 227, 195, 180, 100, 50, 253, 113, 180, 103, 174])

    def test_from_seed_02(self):
        seed: bytes = bytes.fromhex(
            '01f5bced59dec48e362f2c45b5de68b9fd6c92c6634f44d6d40aab69056506f0e35524a518034ddc1192e1dacd32c1ed3eaa3c3b131c88ed8e7e54c49a5d0998')
        chain_code, private_key = Bip32.from_seed(seed)
        self.assertEqual(list(chain_code),
                         [109, 248, 59, 18, 64, 116, 25, 19, 152, 132, 189, 70, 73, 126, 159, 250, 191, 41, 255, 153,
                          124, 132, 176, 14, 91, 81, 140, 208, 97, 8, 164, 39])
        self.assertEqual(list(private_key),
                         [103, 155, 249, 44, 4, 207, 22, 48, 112, 83, 203, 237, 51, 120, 79, 60, 66, 102, 179, 98, 191,
                          95, 61, 126, 225, 59, 237, 111, 39, 25, 116, 60])

    def test_derive_keypair(self):
        seed: bytes = bytes.fromhex(
            '01f5bced59dec48e362f2c45b5de68b9fd6c92c6634f44d6d40aab69056506f0e35524a518034ddc1192e1dacd32c1ed3eaa3c3b131c88ed8e7e54c49a5d0998')
        chain_code, private_key = Bip32.from_seed(seed)
        private_key, public_key = Bip32.derive_keypair(chain_code, private_key)
        self.assertEqual(list(private_key),
                         [228, 190, 224, 79, 196, 220, 97, 44, 25, 94, 149, 235, 197, 132, 45, 145, 79, 210, 128, 40,
                          14, 29, 104, 117, 16, 7, 141, 65, 135, 240, 115, 195])
        self.assertEqual(list(public_key),
                         [2, 201, 161, 156, 87, 230, 51, 65, 92, 85, 70, 202, 248, 75, 26, 2, 255, 165, 43, 210, 191,
                          241, 202, 129, 202, 212, 171, 231, 10, 229, 184, 83, 238])

    def test_derive_keypair_02(self):
        # Ref: https://wolovim.medium.com/ethereum-201-hd-wallets-11d0c93c87f7
        seed: bytes = bytes.fromhex(
            'fffcf9f6f3f0edeae7e4e1dedbd8d5d2cfccc9c6c3c0bdbab7b4b1aeaba8a5a29f9c999693908d8a8784817e7b7875726f6c696663605d5a5754514e4b484542')
        chain_code, private_key = Bip32.from_seed(seed)
        private_key, public_key = Bip32.derive_keypair(chain_code, private_key)
        self.assertEqual(private_key.hex(), '3c4cf049f83a5870ab31c396a0d46783c3e3974da1364ea5a2477548d36b5f8f')
        self.assertEqual(public_key.hex(), '024c8f4044470bd42b81a8b233e2f954b63f4ee2c32c8d44288b44188754e2042e')
