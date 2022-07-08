# crypto-ethereum

My learning on internal working of Ethereum

- Generate 24 "mnemonic" words to construct an arbitrary 256-bit entropy + 8-bit checksum. Each word corresponds to a 11-bit number.
  Alternatively, we can also use 12 mnemonic words to construct 128-bit entropy + 4-bit checksum.
- These mnemonic words are hashed (HMAC) into a 512-bit number called "seed".
- From the seed, we can generate chains of public key and private key pairs deterministically. Ethereum is using a specific path: m/44'/60'/0'/0/0.
- From the 256-bit public key, we can generate the wallet address by getting the last 20 bytes of the Keccak-256 hash of the public key.
