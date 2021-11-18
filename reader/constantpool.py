from reader.binary import read_u2, read_u1


def read_cp_class(file, tag):
    """Read CONSTANT_Class_info structure"""
    return {
        'tag': tag,
        'name_index': read_u2(file)
    }


def read_cp_field_ref_info(file, tag):
    return {
        'tag': tag,
        'class_index': read_u2(file),
        'name_and_type_index': read_u2(file)
    }


def read_cp_method_ref_info(file, tag):
    return {
        'tag': tag,
        'class_index': read_u2(file),
        'name_and_type_index': read_u2(file)
    }


def read_cp_interfacemethod_ref_info(file, tag):
    return {
        'tag': tag,
        'class_index': read_u2(file),
        'name_and_type_index': read_u2(file)
    }


def read_cp_string_info(file, tag):
    return {
        'tag': tag,
        'string_index': read_u2(file)
    }


def read_cp_integer_info(file, tag):
    return {
        'tag': tag,
        'bytes': file.read(4)
    }


def read_cp_float_info(file, tag):
    return {
        'tag': tag,
        'bytes': file.read(4)
    }


def read_cp_long_info(file, tag):
    return {
        'tag': tag,
        'hight_bytes': file.read(4),
        'low_bytes': file.read(4)
    }


def read_cp_double_info(file, tag):
    return {
        'tag': tag,
        'hight_bytes': file.read(4),
        'low_bytes': file.read(4)
    }


def read_cp_nameandtype_info(file, tag):
    return {
        'tag': tag,
        'name_index': read_u2(file),
        'descriptor_index': read_u2(file)
    }


def read_cp_utf8_info(file, tag):
    length = read_u2(file)
    return {
        'tag': tag,
        'length': length,
        'bytes': file.read(length)
    }


def read_cp_methodhandle_info(file, tag):
    return {
        'tag': tag,
        'reference_kind': read_u1(file),
        'reference_index': read_u2(file)
    }


def read_cp_methodtype_info(file, tag):
    return {
        'tag': tag,
        'descriptor_index': read_u2(file)
    }


def read_cp_invokedynamic_info(file, tag):
    return {
        'tag': tag,
        'bootstrap_method_attr_index': read_u2(file),
        'name_and_type_index': read_u2(file)
    }

