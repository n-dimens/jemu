from formatter.classfile import print_class
from reader.classfile import parse_class_file

if __name__ == '__main__':
    with open("HelloWorld.class", "rb") as input_file:
        class_info = parse_class_file(input_file)
    print("\n".join(print_class(class_info)))
