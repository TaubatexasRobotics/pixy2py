class Checksum:
    cs: int = 0
    @staticmethod
    def updateChecksum(b: int) -> None:
        """Adds byte to checksum

        :param b: Byte to be added
        """
        cs += b

    @staticmethod
    def getChecksum() -> int:
        """Returns calculated checksum

        :returns: Calculated checksum
        """
        return cs

    @staticmethod
    def reset() -> None:
        """Returns calculated checksum

        :returns: Calculated checksum
        """
        cs = 0
