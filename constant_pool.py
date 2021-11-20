def get_constant_name(constant_pool, index) -> str:
    return constant_pool[index - 1]['bytes'].decode('utf-8')

