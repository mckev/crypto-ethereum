import unittest

from classes.util import Util


class TestUtil(unittest.TestCase):

    def test_base32encode(self):
        # Ref: https://en.bitcoin.it/wiki/Bech32
        data: bytes = bytes.fromhex('751e76e8199196d454941c45d1b3a323f1433bd6')
        binary: str = Util.bytes_to_bin(data)
        data_in_base32: list[int] = Util.split_bits(binary, 5)
        expected: list[int] = [14, 20, 15, 7, 13, 26, 0, 25, 18, 6, 11, 13, 8, 21, 4, 20, 3, 17, 2, 29, 3, 12, 29, 3, 4,
                               15, 24, 20, 6, 14, 30, 22]
        self.assertEqual(data_in_base32, expected)

    def test_base32encode_02(self):
        data_in_base32: list[int] = Util.split_bits('11100001', 5)
        self.assertEqual(data_in_base32, [7, 1])
