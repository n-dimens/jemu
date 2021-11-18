from typing import BinaryIO

from ConstantPoolTag import ConstantPoolTag
from reader.binary import read_u1
from reader.constantpool import read_cp_class


def read_cp_info(file: BinaryIO) -> dict:
    tag = read_u1(file)
    if tag == ConstantPoolTag.CLASS:
        return read_cp_class(file, tag)
    elif tag == ConstantPoolTag.FIELD_REF:
        return read_cp_fieldref_info(file, tag)

    return {'tag': tag}
