#  TODO: class
from typing import List

from core.constant_pool import ConstantPool


class ClassFile:
    def __init__(self, raw_info):
        self.raw_info = raw_info
        self.constant_pool = ConstantPool(raw_info['constant_pool'])
        self.magic = raw_info['magic']
        self.minor_version = raw_info['minor_version']
        self.major_version = raw_info['minor_version']
        self.this_class = self.constant_pool.get_class_name(self.raw_info['this_class'])
        self.super_class = self.constant_pool.get_class_name(self.raw_info['super_class'])

        self.attributes = self.extend_list('attributes')
        self.fields = self.extend_list('fields')
        self.methods = self.extend_list('methods')

    def extend_list(self, list_name: str):
        extender = None
        if list_name == 'attributes':
            extender = self.extend_attribute_info
        elif list_name == 'fields':
            extender = self.extend_field_info
        elif list_name == 'methods':
            extender = self.extend_method_info

        return [extender(mi) for mi in self.raw_info[list_name]]

    def extend_field_info(self, raw_info):
        # TODO: access_flags to array enum
        field_info = {
            'access_flags': raw_info['access_flags'],
            'name': self.constant_pool.get_constant_name(raw_info['name_index']),
            'descriptor': self.constant_pool.get_constant_name(raw_info['descriptor_index']),
            'attributes': []
        }

        for i in range(raw_info['attributes_count']):
            raw_attribute_info = raw_info['attributes_info'][i]
            field_info['attributes'].append(self.extend_method_info(raw_attribute_info))

        return field_info

    def extend_method_info(self, raw_info):
        # TODO: access_flags to array enum
        method_info = {
            'access_flags': raw_info['access_flags'],
            'name': self.constant_pool.get_constant_name(raw_info['name_index']),
            'descriptor': self.constant_pool.get_constant_name(raw_info['descriptor_index']),
            'attributes': []
        }

        for i in range(raw_info['attributes_count']):
            raw_attribute_info = raw_info['attributes_info'][i]
            method_info['attributes'].append(self.extend_attribute_info(raw_attribute_info))

        method_info['code'] = [attr['code'] for attr in method_info['attributes'] if attr['name'] == 'Code']
        return method_info

    def extend_attribute_info(self, raw_info):
        name: str = self.constant_pool.get_constant_name(raw_info['name_index'])
        attribute_info = {'name': name}
        if name == 'SourceFile':
            attribute_info['file_name'] = self.extend_source_file_attr(raw_info)
        elif name == 'Code':
            attribute_info['code'] = CodeAttributeExtender(self.constant_pool).extend(raw_info['info'])

        return attribute_info

    def extend_source_file_attr(self, raw_info):
        name_index = int.from_bytes(raw_info['info'], "big")
        return self.constant_pool.get_constant_name(name_index)


class CodeAttributeExtender:
    def __init__(self, constant_pool):
        self.constant_pool = constant_pool

    def extend(self, raw_info: bytearray):
        code_info = {
            'max_stack': read_u2(raw_info, 0),
            'max_locals': read_u2(raw_info, 2),
            'size': len(raw_info)
        }

        code_length = read_u4(raw_info, 4)
        code_last_index = 8 + code_length
        code_info['code_length'] = code_length
        code_info['code'] = raw_info[8:code_last_index]

        exceptions_length = read_u2(raw_info, code_last_index)
        exceptions_last_index = 2 + code_last_index + exceptions_length
        code_info['exceptions'] = raw_info[(code_last_index + 2):exceptions_last_index]

        attributes_count = read_u2(raw_info, exceptions_last_index)
        code_info['attributes_count'] = attributes_count
        code_info['attributes'] = raw_info[exceptions_last_index:(exceptions_last_index + attributes_count)]
        return code_info


def read_u1(bytes_: bytearray, index: int) -> int:
    return read_int(bytes_, index, 1)


def read_u2(bytes_: bytearray, index: int) -> int:
    return read_int(bytes_, index, 2)


def read_u4(bytes_: bytearray, index: int) -> int:
    return read_int(bytes_, index, 4)


def read_int(bytes_: bytearray, index: int, length: int) -> int:
    return int.from_bytes(bytes_[index:(index + length)], "big")
