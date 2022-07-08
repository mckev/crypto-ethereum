class Util:

    @staticmethod
    def split_bits(b: bytes, n: int) -> list[int]:
        """ Split bytes into a list of n-bit integers """
        # Convert to binary
        binary: str = ''
        for i in b:
            binary += bin(i).lstrip('0b').zfill(8)
        # Split
        parts: list[int] = []
        while len(binary) > 0:
            part: str = binary[-n:]
            parts.insert(0, int(part, 2))
            binary = binary[:-n]
        return parts
