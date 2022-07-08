# crypto-ethereum

My learning on internal working of Ethereum

- Generate 24 "mnemonic" words to construct an arbitrary 256-bit entropy + 8-bit checksum. Each word corresponds to a 11-bit number.
  Alternatively, we can also use 12 mnemonic words to construct 128-bit entropy + 4-bit checksum.
- These mnemonic words are hashed (HMAC) into a 512-bit number called "seed".
- From the seed, we can generate chains of public key and private key pairs deterministically. Ethereum is using a specific path: m/44'/60'/0'/0/0.
- From the 256-bit public key, we can generate the wallet address by getting the last 20 bytes (160-bit) of the Keccak-256 hash of the public key.
- For checksummed wallet address, we hash the hexed wallet address with Keccak-256. If the hashed character is '8', '9', 'a', 'b', 'c', 'd', 'e', 'f' then we uppercase the character.

Using the above, I can generate wallet addresses which end with a chosen suffix :).
