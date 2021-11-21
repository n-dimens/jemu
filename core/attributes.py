from core.instructions import obtain_instruction
from reader.binary import CollectionReader, bytes_to_int, read_u4, read_u2


def read_attribute_info(reader) -> dict:
    """reader must have method read(count: int) -> bytes"""
    attribute_info = {
        'name_index': read_u2(reader),
        'length': read_u4(reader)
    }
    attribute_info['info'] = reader.read(attribute_info['length'])
    return attribute_info


def extend_attribute_info(constant_pool, raw_info):
    name: str = constant_pool.get_constant_name(raw_info['name_index'])
    attribute_info = {'name': name}
    if name == 'SourceFile':
        attribute_info['file_name'] = extend_source_file_attr(constant_pool, raw_info)
    elif name == 'Code':
        attribute_info['code'] = extend_code_attr(constant_pool, raw_info)
    elif name == 'LineNumberTable':
        attribute_info['table'] = extend_line_number_table_attr(raw_info)

    return attribute_info


def extend_source_file_attr(constant_pool, raw_info):
    name_index = bytes_to_int(raw_info['info'])
    return constant_pool.get_constant_name(name_index)


def extend_code_attr(constant_pool, raw_info):
    info = raw_info['info']
    reader = CollectionReader(info)
    code_info = {
        'max_stack': bytes_to_int(reader.read(2)),
        'max_locals': bytes_to_int(reader.read(2)),
        'size': len(info)
    }

    code_length = bytes_to_int(reader.read(4))
    code_info['code_length'] = code_length
    code_info['code'] = reader.read(code_length)
    parse_code(code_info['code'])

    exceptions_length = bytes_to_int(reader.read(2))
    code_info['exceptions'] = reader.read(exceptions_length)

    attributes_count = bytes_to_int(reader.read(2))
    code_info['attributes'] = []
    for i in range(attributes_count):
        raw_attribute = read_attribute_info(reader)
        code_info['attributes'].append(extend_attribute_info(constant_pool, raw_attribute))

    return code_info


def parse_code(raw_code):
    reader = CollectionReader(raw_code)
    while reader.has_next():
        opcode = bytes_to_int(reader.read(1))
        print(obtain_instruction(opcode, reader))


def extend_line_number_table_attr(raw_info):
    info = raw_info['info']
    reader = CollectionReader(info)
    table_length = bytes_to_int(reader.read(2))
    table = []
    for i in range(table_length):
        table.append({
            'start_pc': bytes_to_int(reader.read(2)),
            'line_number': bytes_to_int(reader.read(2))
        })
    return table
