def get_constant_name(constant_pool, index) -> str:
    return constant_pool[index - 1]['bytes'].decode('utf-8')


def get_class_name(constant_pool, index) -> str:
    class_info = constant_pool[index - 1]
    return get_constant_name(constant_pool, class_info['name_index'])


class ConstantPool:
    def __init__(self, info):
        self.info = info

    def get_class_name(self, index) -> str:
        class_info = self.info[index - 1]
        return self.get_constant_name(class_info['name_index'])

    def get_constant_name(self, index):
        return self.info[index - 1]['bytes'].decode('utf-8')
