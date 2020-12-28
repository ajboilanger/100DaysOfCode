from abc import ABC, abstractmethod


class InvalidOperationError(Exception):  # Creates a custom exception class
    pass


class Stream(ABC):  # Creates a Stream class
    def __init__(self):
        self.opened = False  # Sets the default value of opened to False, indicating it's closed

    def open(self):
        if self.opened:  # Checks to see if the stream is not already open
            # Uses our custom exception class.
            raise InvalidOperationError("Stream is already open.")
        self.opened = True  # Sets stream to open

    def close(self):
        if not self.opened:  # Checks to see if the stream is not already closed
            # Uses our custom exception class.
            raise InvalidOperationError("Stream is already closed.")
        self.opened = False  # Sets stream to closed

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from a file.")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network.")


class MemoryStream(Stream):
    def read(self):
        print("Reading data from a memory stream.")


stream = MemoryStream()
stream.open()

"""
An abstract base class can be used to help enforce standards throughout classes.
"""
