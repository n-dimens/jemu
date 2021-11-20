from collections import namedtuple
from enums import ConstantPoolTag
from reader.binary import read_u4, read_u2
from reader.classfile import read_cp_info, read_field_info, read_method_info, read_attribute_info


def parse_class_file(file_path):
    """Загрузка class-файла"""
    class_file = {}
    with open(file_path, "rb") as file:
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


def print_class(class_file):
    print(f"{class_file['major_version']}.{class_file['minor_version']}")
    print(f"access: {hex(class_file['access_flags'])}")

    constant_pool = class_file['constant_pool']
    this_class_info = constant_pool[class_file['this_class'] - 1]
    # print(this_class_info)
    this_class_name = constant_pool[this_class_info['name_index'] - 1]['bytes'].decode('utf-8')
    print(f"Class: {this_class_name}")

    super_class_info = constant_pool[class_file['super_class'] - 1]
    # print(this_class_info)
    super_class_name = constant_pool[super_class_info['name_index'] - 1]['bytes'].decode('utf-8')
    print(f"Super class: {super_class_name}")

    print(f"Constant pool count: {class_file['constant_pool_count'] - 1}")
    # for i in range(len(class_file['constant_pool'])):
    #     cp_info = class_file['constant_pool'][i - 1]
    #     tag = ConstantPoolTag(cp_info['tag']).name
    #     print(f"#{i + 1} = {tag}\t{cp_info}")

    print(f"Interfaces count: {class_file['interfaces_count']}")
    print(f"Fields count: {class_file['fields_count']}")
    print(f"Methods count: {class_file['methods_count']}")
    print(f"Class attributes count: {class_file['attributes_count']}")
    for i in range(class_file['attributes_count']):
        print_attribute_info(constant_pool, class_file['attributes'][i])


def print_attribute_info(constant_pool, attribute_info):
    attribute_name = constant_pool[attribute_info['name_index'] - 1]['bytes'].decode('utf-8')
    attribute_value = ""
    if attribute_name == "SourceFile":
        file_name_index = int.from_bytes(attribute_info['info'], "big")
        attribute_value = constant_pool[file_name_index - 1]['bytes'].decode('utf-8')
    print(f"\t{attribute_name}: {attribute_value}")
    pass


if __name__ == '__main__':
    class_info = parse_class_file("HelloWorld.class")
    print_class(class_info)
