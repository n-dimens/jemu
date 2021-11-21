from core.attributes import extend_attribute_info
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

        self.attributes = self.extend_table('attributes')
        self.fields = self.extend_table('fields')
        self.methods = self.extend_table('methods')

    def extend_table(self, list_name: str):
        extender = None
        if list_name == 'attributes':
            return [extend_attribute_info(self.constant_pool, mi) for mi in self.raw_info[list_name]]

        if list_name == 'fields':
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
            method_info['attributes'].append(extend_attribute_info(self.constant_pool, raw_attribute_info))

        method_info['code'] = [attr['code'] for attr in method_info['attributes'] if attr['name'] == 'Code']
        return method_info
