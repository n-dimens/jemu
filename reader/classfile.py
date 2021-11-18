from typing import BinaryIO

from ConstantPoolTag import ConstantPoolTag
from reader.constantpool import *


def read_cp_info(file: BinaryIO) -> dict:
    tag = ConstantPoolTag(read_u1(file))
    if tag == ConstantPoolTag.CLASS:
        return read_cp_class(file, tag)
    elif tag == ConstantPoolTag.FIELD_REF:
        return read_cp_field_ref_info(file, tag)
    elif tag == ConstantPoolTag.METHOD_REF:
        return read_cp_method_ref_info(file, tag)
    elif tag == ConstantPoolTag.INTERFACE_METHOD_REF:
        return read_cp_interfacemethod_ref_info(file, tag)
    elif tag == ConstantPoolTag.STRING:
        return read_cp_string_info(file, tag)
    elif tag == ConstantPoolTag.INTEGER:
        return read_cp_integer_info(file, tag)
    elif tag == ConstantPoolTag.FLOAT:
        return read_cp_float_info(file, tag)
    elif tag == ConstantPoolTag.LONG:
        return read_cp_long_info(file, tag)
    elif tag == ConstantPoolTag.DOUBLE:
        return read_cp_double_info(file, tag)
    elif tag == ConstantPoolTag.NAME_AND_TYPE:
        return read_cp_nameandtype_info(file, tag)
    elif tag == ConstantPoolTag.UTF8:
        return read_cp_utf8_info(file, tag)
    elif tag == ConstantPoolTag.METHOD_HANDLE:
        return read_cp_methodhandle_info(file, tag)
    elif tag == ConstantPoolTag.METHOD_TYPE:
        return read_cp_methodtype_info(file, tag)
    elif tag == ConstantPoolTag.INVOKE_DYNAMIC:
        return read_cp_invokedynamic_info(file, tag)

    raise Exception(f"Unknown constant pool tag '{tag}'")
