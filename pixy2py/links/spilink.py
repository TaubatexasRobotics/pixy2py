from links.link import Link
from wpilib import SPI
from typing import Optional
from checksum import Checksum

class SPILink(Link):
    PIXY_SPI_CLOCKRATE: int = 2000000;

    def __init__(self) -> None:
        self._spi: Optional[SPI] = None

    def open(self, arg: int) -> int:
        """Opens SPI port

        :param arg: SPI port

        :returns: Returns 0
        """
        port = None
        match arg:
            case 1:
                port = SPI.Port.kOnboardCS1
            case 2:
                port = SPI.Port.kOnboardCS2
            case 3:
                port = SPI.Port.kOnBoardCS3
            case 4:
                port = SPI.Port.kMXP
            case _:
                port = SPI.Port.kOnBoardCS0
        self._spi = SPI(port)
        self._spi.setClockRate(PIXY_SPI_CLOCKRATE)
        self._spi.setMSBFirst()
        self._spi.setSampleDataOnTrailingEdge()
        self._spi.setClockActiveLow()
        self._spi.setChipSelectActiveLow()
        return 0

    def close(self) -> None:
        """Closes SPI port"""
        self._spi.close()

    def receive(self, buffer: bytearray, length: int, cs: Optional[Checksum] =None) -> int:
        """Receives and reads specified length of bytes from SPI

        :param buffer: Byte buffer to return value
        :param length: Length of value to read
        :param cs:     Checksum

        :returns: Length of value read
        """
        if cs is not None:
            cs.reset()

        self._spi.read(False, buffer, length)

        if cs is not None:
            for b in buffer[:length]:
                cs.update_checksum(b)

        return length

    def send(self, buffer: bytearray, lenght: int) -> int:
        """Writes and sends buffer over SPI

        :param buffer: Byte buffer to send
        :param length: Length of value to send

        :returns: Length of value sent
        """

