from reader.binary import read_u2


def read_cp_class(file, tag):
    """Read CONSTANT_Class_info structure"""
    return {
        'tag': tag,
        'name_index': read_u2(file)
    }


def read_cp_fieldref_info(file, tag):
    return {
        'tag': tag,
        'class_index': read_u2(file),
        'name_and_type_index': read_u2(file)
    }
