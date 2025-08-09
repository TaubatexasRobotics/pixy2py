class Checksum:
    cs = 0
    @staticmethod
    def updateChecksum(b: int) -> None:
        cs += b

    @staticmethod
    def getChecksum() -> int:
        return cs

    @staticmethod
    def reset() -> None:
        cs = 0
