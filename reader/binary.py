from typing import BinaryIO


def read_bytes(file, size: int) -> int:
    return bytes_to_int(file.read(size))


def read_u1(file) -> int:
    return read_bytes(file, 1)


def read_u2(file) -> int:
    return read_bytes(file, 2)


def read_u4(file) -> int:
    return read_bytes(file, 4)


def bytes_to_int(bytes_: bytes) -> int:
    return int.from_bytes(bytes_, "big", signed=False)


class CollectionReader:
    def __init__(self, data):
        self.data = data
        self.position = 0

    def read(self, length):
        right = self.position + length
        if right > len(self.data):
            right = len(self.data)

        data = self.data[self.position:right]
        self.position += length
        return data

    def has_next(self):
        return self.position < len(self.data)
