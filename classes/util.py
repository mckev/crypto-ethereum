class Util:

    @staticmethod
    def bytes_to_bin(data: bytes) -> str:
        output: str = ''
        for b in data:
            output += bin(b).lstrip('0b').zfill(8)
        return output

    @staticmethod
    def split_bits(binary: str, n: int) -> list[int]:
        """ Split binary into a list of n-bit integers """
        parts: list[int] = []
        while len(binary) > 0:
            part: str = binary[-n:]
            parts.insert(0, int(part, 2))
            binary = binary[:-n]
        return parts
