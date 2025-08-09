from ..checksum import Checksum
from abc import ABC, abstractmethod

class Link:
    @abstractmethod
    def open(self, arg: int) -> None:
        """Opens link

        :param arg: Link argument

        :returns: Returns state
        """
        pass
    
    @abstractmethod
    def close(self) -> None:
        """Closes link"""
        pass
    
    @abstractmethod
    def receive(self, buffer: bytearray, length: int, cs: Checksum) -> int:
        """Receives and reads specified length of bytes over link

        :param buffer: Byte buffer to return value
        :param length: Length of value to read
        :param cs:     Checksum

        :returns: Length of value read
        """
        pass

    @abstractmethod
    def send(self, buffer: bytearray, length: int) -> int:
        """Writes and sends buffer over link

        :param buffer: Byte buffer to send
        :param length: Length of value to send

        :returns: Length of value sent
        """
        pass
