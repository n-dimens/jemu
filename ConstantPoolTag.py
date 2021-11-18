from enum import Enum


class ConstantPoolTag(Enum):
    CLASS = 7
    FIELD_REF = 9
    METHOD_REF = 10
    INTRFACE_METHOD_REF = 11
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
