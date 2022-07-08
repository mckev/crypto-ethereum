import Crypto.Hash.keccak  # pip install pycryptodome
import coincurve

from classes.bip32 import Bip32
from classes.bip39 import Bip39


class Ethereum:

    @staticmethod
    def keccak256(message: bytes) -> bytes:
        keccak = Crypto.Hash.keccak.new(data=message, digest_bits=256)
        return keccak.digest()

    @staticmethod
    def create_ethereum_address(public_key: bytes) -> str:
        # https://www.freecodecamp.org/news/how-to-create-an-ethereum-wallet-address-from-a-private-key-ae72b0eee27b/
        public_key = coincurve.PublicKey(public_key)
        x, y = public_key.point()
        x_in_bytes: bytes = x.to_bytes(32, byteorder='big')
        y_in_bytes: bytes = y.to_bytes(32, byteorder='big')
        # Ethereum public address is the last 20 bytes of the Keccak-256 hash of the public key
        ethereum_address_in_bytes: bytes = Ethereum.keccak256(x_in_bytes + y_in_bytes)[-20:]
        return Ethereum.checksum_ethereum_address(ethereum_address_in_bytes)

    @staticmethod
    def checksum_ethereum_address(ethereum_address_in_bytes: bytes) -> str:
        # Ref: https://github.com/ethereum/EIPs/blob/master/EIPS/eip-55.md
        ethereum_address_in_str: str = '0x'
        hashed_address: bytes = Ethereum.keccak256(ethereum_address_in_bytes.hex().encode(encoding='ascii'))
        for ch, hash in zip(ethereum_address_in_bytes.hex(), hashed_address.hex()):
            if hash in ['8', '9', 'a', 'b', 'c', 'd', 'e', 'f']:
                ethereum_address_in_str += ch.upper()
            else:
                ethereum_address_in_str += ch
        return ethereum_address_in_str

    @staticmethod
    def generate_wallet(mnemonics: list[str]) -> any:
        seed: bytes = Bip39.mnemonics_to_seed(mnemonics)
        chain_code, private_key = Bip32.from_seed(seed)
        private_key, public_key = Bip32.derive_keypair(chain_code, private_key)
        ethereum_address: str = Ethereum.create_ethereum_address(public_key)
        return {
            'private_key': private_key.hex(),
            'public_key': public_key.hex(),
            'ethereum_address': ethereum_address
        }
