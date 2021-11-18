from ConstantPoolTag import ConstantPoolTag
from reader.binary import read_u4, read_u2
from reader.classfile import read_cp_info


def parse_class_file(file_path):
    """Загрузка class-файла"""
    class_file = {}
    with open(file_path, "rb") as file:
        class_file['magic'] = read_u4(file)
        class_file['minor_version'] = read_u2(file)
        class_file['major_version'] = read_u2(file)
        constant_pool_count = read_u2(file)
        class_file['constant_pool'] = []
        for i in range(1, constant_pool_count - 1):
            class_file['constant_pool'].append(read_cp_info(file))

    print(f"{class_file['major_version']}.{class_file['minor_version']}")
    for i in range(0, len(class_file['constant_pool']) - 2):
        tag = ConstantPoolTag(class_file['constant_pool'][i]['tag']).name
        print(f"Tag: {tag}")


if __name__ == '__main__':
    parse_class_file("HelloWorld.class")
