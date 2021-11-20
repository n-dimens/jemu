from attributes.source_file import as_source_file
from constant_pool import get_constant_name

__all__ = ['print_class']


def print_class(class_file) -> [str]:
    result = [
        f"{class_file['major_version']}.{class_file['minor_version']}",
        f"access: {hex(class_file['access_flags'])}"
    ]

    constant_pool = class_file['constant_pool']
    this_class_info = constant_pool[class_file['this_class'] - 1]
    this_class_name = get_constant_name(constant_pool, this_class_info['name_index'])
    result.append(f"Class: {this_class_name}")

    super_class_info = constant_pool[class_file['super_class'] - 1]

    super_class_name = get_constant_name(constant_pool, super_class_info['name_index'])
    result.append(f"Super class: {super_class_name}")

    result.append(f"Constant pool count: {class_file['constant_pool_count'] - 1}")
    # for i in range(len(class_file['constant_pool'])):
    #     cp_info = class_file['constant_pool'][i - 1]
    #     tag = ConstantPoolTag(cp_info['tag']).name
    #     print(f"#{i + 1} = {tag}\t{cp_info}")

    result.append(f"Interfaces count: {class_file['interfaces_count']}")
    result.append(f"Fields count: {class_file['fields_count']}")
    result.append(f"Methods count: {class_file['methods_count']}")
    result.append(f"Class attributes count: {class_file['attributes_count']}")
    for i in range(class_file['attributes_count']):
        result += indent_text(format_attribute_info(constant_pool, class_file['attributes'][i]), 1)
    return result


def format_attribute_info(constant_pool, attribute_info) -> [str]:
    attribute_name = get_constant_name(constant_pool, attribute_info['name_index'])
    attribute_formatter = get_attribute_formatter(attribute_name)
    return attribute_formatter(constant_pool, attribute_info)


def get_attribute_formatter(attribute_name):
    if attribute_name == "SourceFile":
        return format_sourcefile_attribute


def format_sourcefile_attribute(constant_pool, attribute_info) -> [str]:
    """Formatting 'SourceFile' attribute"""
    source_file = as_source_file(attribute_info)
    file_name = get_constant_name(constant_pool, source_file['name_index'])
    return [f"SourceFile: {file_name}"]


def indent_text(text: [str], length: int) -> [str]:
    return ["\t" * length + row for row in text]
