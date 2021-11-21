from typing import BinaryIO

from core.attributes import read_attribute_info
from core.enums import ConstantPoolTag
from reader.binary import read_u4
from reader.constantpool import *


def parse_class_file(file: BinaryIO) -> dict:
    """Чтение class-файла"""
    class_file = {}
    class_file['magic'] = read_u4(file)
    class_file['minor_version'] = read_u2(file)
    class_file['major_version'] = read_u2(file)
    class_file['constant_pool_count'] = read_u2(file)
    class_file['constant_pool'] = []
    for i in range(class_file['constant_pool_count'] - 1):
        class_file['constant_pool'].append(read_cp_info(file))
    class_file['access_flags'] = read_u2(file)
    class_file['this_class'] = read_u2(file)
    class_file['super_class'] = read_u2(file)
    class_file['interfaces_count'] = read_u2(file)
    class_file['interfaces'] = []
    for i in range(class_file['interfaces_count']):
        class_file['interfaces'].append(read_u2(file))

    class_file['fields_count'] = read_u2(file)
    class_file['fields'] = []
    for i in range(class_file['fields_count']):
        class_file['fields'].append(read_field_info(file))

    class_file['methods_count'] = read_u2(file)
    class_file['methods'] = []
    for i in range(class_file['methods_count']):
        class_file['methods'].append(read_method_info(file))

    class_file['attributes_count'] = read_u2(file)
    class_file['attributes'] = []
    for i in range(class_file['attributes_count']):
        class_file['attributes'].append(read_attribute_info(file))

    return class_file


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


def read_field_info(file):
    field_info = {
        'access_flags': read_u2(file),
        'name_index': read_u2(file),
        'descriptor_index': read_u2(file),
        'attributes_count': read_u2(file),
        'attributes_info': []
    }
    for i in range(field_info['attributes_count']):
        field_info['attributes_info'].append(read_attribute_info(file))
    return field_info


def read_method_info(file):
    method_info = {
        'access_flags': read_u2(file),
        'name_index': read_u2(file),
        'descriptor_index': read_u2(file),
        'attributes_count': read_u2(file),
        'attributes_info': []
    }
    for i in range(method_info['attributes_count']):
        method_info['attributes_info'].append(read_attribute_info(file))
    return method_info

