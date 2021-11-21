#!/usr/bin/env python
import pprint

from core.class_file import ClassFile
from formatter.classfile import format_raw_class
from reader.classfile import parse_class_file


def read_raw_info(file_path: str) -> dict:
    with open(file_path, "rb") as input_file:
        return parse_class_file(input_file)


if __name__ == '__main__':
    raw_class_info = read_raw_info("resources/HelloWorld.class")
    class_info = ClassFile(raw_class_info)
    # pprint.pprint(class_info.methods)
    for m in class_info.methods:
        print(f"{m['name']} : {m['descriptor']}")
        print(m['code'])
    # print("\n".join(format_raw_class(raw_class_info)))
