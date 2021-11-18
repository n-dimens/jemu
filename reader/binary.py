from typing import BinaryIO


def read_bytes(file: BinaryIO, size: int) -> int:
    return int.from_bytes(file.read(size), "big")


def read_u1(file: BinaryIO) -> int:
    return read_bytes(file, 1)


def read_u2(file: BinaryIO) -> int:
    return read_bytes(file, 2)


def read_u4(file: BinaryIO) -> int:
    return read_bytes(file, 4)
