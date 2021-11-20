from enum import Enum


class ConstantPoolTag(Enum):
    CLASS = 7
    FIELD_REF = 9
    METHOD_REF = 10
    INTERFACE_METHOD_REF = 11
    STRING = 8
    INTEGER = 3
    FLOAT = 4
    LONG = 5
    DOUBLE = 6
    NAME_AND_TYPE = 12
    UTF8 = 1
    METHOD_HANDLE = 15
    METHOD_TYPE = 16
    INVOKE_DYNAMIC = 18


class ClassAccess(Enum):
    PUBLIC = 0x0001
    FINAL = 0x0010
    SUPER = 0x0020
    INTERFACE = 0x0200
    ABSTRACT = 0x0400
    SYNTHETIC = 0x1000
    ANNOTATION = 0x2000
    ENUM = 0x4000


class FieldAccess(Enum):
    PUBLIC = 0x0001
    PRIVATE = 0x0002
    PROTECTED = 0x0004
    STATIC = 0x0008
    FINAL = 0x0010
    VOLATILE = 0x0040
    TRANSIENT = 0x0080
    SYNTHETIC = 0x1000
    ENUM = 0x4000


class MethodAccess(Enum):
    PUBLIC = 0x0001
    PRIVATE = 0x0002
    PROTECTED = 0x0004
    STATIC = 0x0008
    FINAL = 0x0010
    SYNCHRONIZED = 0x0020
    BRIDGE = 0x0040
    VARARGS = 0x0080
    NATIVE = 0x0100
    ABSTRACT = 0x0400
    STRICT = 0x0800
    SYNTHETIC = 0x1000
