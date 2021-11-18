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
        class_file['constant_pool'] = {}
        # for i in range(1, constant_pool_count - 1):
        #     p = read_cp_info(file)
        #     pass

    print(f"{class_file['major_version']}.{class_file['minor_version']}")


if __name__ == '__main__':
    parse_class_file("HelloWorld.class")
