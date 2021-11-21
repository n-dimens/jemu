from reader.binary import bytes_to_int


def obtain_instruction(opcode, reader):
    instruction = {"code": opcode, 'name': '', 'args': []}
    if opcode == 0x32:
        instruction['name'] = "aaload"
    elif opcode == 0x53:
        instruction['name'] = "aastore"
    elif opcode == 0x1:
        instruction['name'] = "aconst_null"
    elif opcode == 0x19:
        instruction['name'] = "aload"
        instruction['args'] = [read_unsigned_8(reader)]
    elif opcode == 0x2a:
        instruction['name'] = "aload_0"
    elif opcode == 0x2b:
        instruction['name'] = "aload_1"
    elif opcode == 0x2c:
        instruction['name'] = "aload_2"
    elif opcode == 0x2d:
        instruction['name'] = "aload_3"
    elif opcode == 0xbd:
        instruction['name'] = "anewarray"
        instruction['args'] = [read_signed_16(reader)]
    elif opcode == 0xb0:
        instruction['name'] = "areturn"
    elif opcode == 0xbe:
        instruction['name'] = "arraylength"
    elif opcode == 0x3a:
        instruction['name'] = "astore"
    elif opcode == 0x4b:
        instruction['name'] = "astore_0"
    elif opcode == 0x4c:
        instruction['name'] = "astore_1"
    elif opcode == 0x4d:
        instruction['name'] = "astore_2"
    elif opcode == 0x4e:
        instruction['name'] = "astore_3"
    elif opcode == 0xbd:
        instruction['name'] = "athrow"
    elif opcode == 0x33:
        instruction['name'] = "baload"
    elif opcode == 0x54:
        instruction['name'] = "bastore"
    elif opcode == 0x54:
        instruction['name'] = "bipush"
        instruction['args'] = [read_unsigned_8(reader)]
    elif opcode == 0x34:
        instruction['name'] = "caload"
    elif opcode == 0x55:
        instruction['name'] = "castore"
    elif opcode == 0xc0:
        instruction['name'] = "checkcast"
        instruction['args'] = [read_signed_16(reader)]
    elif opcode == 0x90:
        instruction['name'] = "d2f"
    elif opcode == 0x8e:
        instruction['name'] = "d2i"
    elif opcode == 0x8f:
        instruction['name'] = "d2l"
    elif opcode == 0x63:
        instruction['name'] = "dadd"
    elif opcode == 0x31:
        instruction['name'] = "daload"
    elif opcode == 0x52:
        instruction['name'] = "dastore"
    elif opcode == 0x98:
        instruction['name'] = "dcmpg"
    elif opcode == 0x97:
        instruction['name'] = "dcmpl"
    elif opcode == 0xe:
        instruction['name'] = "dconst_0"
    elif opcode == 0xf:
        instruction['name'] = "dconst_1"
    elif opcode == 0x6f:
        instruction['name'] = "ddiv"
    elif opcode == 0x18:
        instruction['name'] = "dload"
        instruction['args'] = [read_unsigned_8(reader)]
    elif opcode == 0x26:
        instruction['name'] = "dload_0"
    elif opcode == 0x27:
        instruction['name'] = "dload_1"
    elif opcode == 0x28:
        instruction['name'] = "dload_2"
    elif opcode == 0x29:
        instruction['name'] = "dload_3"
    elif opcode == 0x6b:
        instruction['name'] = "dmul"
    elif opcode == 0x77:
        instruction['name'] = "dneg"
    elif opcode == 0x73:
        instruction['name'] = "drem"
    elif opcode == 0xaf:
        instruction['name'] = "dreturn"
    elif opcode == 0x39:
        instruction['name'] = "dstore"
        instruction['args'] = [read_unsigned_8(reader)]
    elif opcode == 0x47:
        instruction['name'] = "dstore_0"
    elif opcode == 0x48:
        instruction['name'] = "dstore_1"
    elif opcode == 0x49:
        instruction['name'] = "dstore_2"
    elif opcode == 0x4a:
        instruction['name'] = "dstore_3"
    elif opcode == 0x67:
        instruction['name'] = "dsub"
    elif opcode == 0x59:
        instruction['name'] = "dup"
    elif opcode == 0x5a:
        instruction['name'] = "dup_x1"
    elif opcode == 0x5b:
        instruction['name'] = "dup_x2"
    elif opcode == 0x5c:
        instruction['name'] = "dup2"
    elif opcode == 0x5d:
        instruction['name'] = "dup2_x1"
    elif opcode == 0x5e:
        instruction['name'] = "dup2_x2"
    elif opcode == 0x8d:
        instruction['name'] = "f2d"
    elif opcode == 0x8b:
        instruction['name'] = "f2i"
    elif opcode == 0x8c:
        instruction['name'] = "f2l"
    elif opcode == 0x62:
        instruction['name'] = "fadd"
    elif opcode == 0x30:
        instruction['name'] = "faload"
    elif opcode == 0x51:
        instruction['name'] = "fastore"
    elif opcode == 0x96:
        instruction['name'] = "fcmpg"
    elif opcode == 0x95:
        instruction['name'] = "fcmpl"
    elif opcode == 0xb:
        instruction['name'] = "fconst_0"
    elif opcode == 0xc:
        instruction['name'] = "fconst_1"
    elif opcode == 0xd:
        instruction['name'] = "fconst_2"
    elif opcode == 0x6e:
        instruction['name'] = "fdiv"
    elif opcode == 0x17:
        instruction['name'] = "fload"
        instruction['args'] = [read_unsigned_8(reader)]
    elif opcode == 0x22:
        instruction['name'] = "fload_0"
    elif opcode == 0x23:
        instruction['name'] = "fload_1"
    elif opcode == 0x24:
        instruction['name'] = "fload_2"
    elif opcode == 0x25:
        instruction['name'] = "fload_3"
    elif opcode == 0x6a:
        instruction['name'] = "fmul"
    elif opcode == 0x76:
        instruction['name'] = "fneg"
    elif opcode == 0x72:
        instruction['name'] = "frem"
    elif opcode == 0xae:
        instruction['name'] = "freturn"
    elif opcode == 0x38:
        instruction['name'] = "fstore"
        instruction['args'] = [read_unsigned_8(reader)]
    elif opcode == 0x43:
        instruction['name'] = "fstore_0"
    elif opcode == 0x44:
        instruction['name'] = "fstore_1"
    elif opcode == 0x45:
        instruction['name'] = "fstore_2"
    elif opcode == 0x46:
        instruction['name'] = "fstore_3"
    elif opcode == 0x66:
        instruction['name'] = "fsub"
    elif opcode == 0xb4:
        instruction['name'] = "getfield"
        instruction['args'] = [read_signed_16(reader)]
    elif opcode == 0xb2:
        instruction['name'] = "getstatic"
        instruction['args'] = [read_signed_16(reader)]
    elif opcode == 0xa7:
        instruction['name'] = "goto"
        instruction['args'] = [read_signed_16(reader)]
    elif opcode == 0xc8:
        instruction['name'] = "goto_w"
        instruction['args'] = [read_signed_32(reader)]
    elif opcode == 0x91:
        instruction['name'] = "i2b"
    elif opcode == 0x92:
        instruction['name'] = "i2c"
    elif opcode == 0x87:
        instruction['name'] = "i2d"
    elif opcode == 0x86:
        instruction['name'] = "i2f"
    elif opcode == 0x85:
        instruction['name'] = "i2l"
    elif opcode == 0x93:
        instruction['name'] = "i2s"
    elif opcode == 0x60:
        instruction['name'] = "iadd"
    elif opcode == 0x2e:
        instruction['name'] = "iaload"
    elif opcode == 0x7e:
        instruction['name'] = "iand"
    elif opcode == 0x4f:
        instruction['name'] = "iastore"
    elif opcode == 0x2:
        instruction['name'] = "iconst_m1"
    elif opcode == 0x3:
        instruction['name'] = "iconst_0"
    elif opcode == 0x4:
        instruction['name'] = "iconst_1"
    elif opcode == 0x5:
        instruction['name'] = "iconst_2"
    elif opcode == 0x6:
        instruction['name'] = "iconst_3"
    elif opcode == 0x7:
        instruction['name'] = "iconst_4"
    elif opcode == 0x8:
        instruction['name'] = "iconst_5"
    elif opcode == 0x6c:
        instruction['name'] = "idiv"
    elif opcode == 0xa5:
        instruction['name'] = "if_acmpeq"
        instruction['args'] = [read_signed_16(reader)]
    elif opcode == 0xa6:
        instruction['name'] = "if_acmpne"
        instruction['args'] = [read_signed_16(reader)]
    elif opcode == 0x9f:
        instruction['name'] = "if_icmpeq"
        instruction['args'] = [read_signed_16(reader)]
    elif opcode == 0xa0:
        instruction['name'] = "if_icmpne"
        instruction['args'] = [read_signed_16(reader)]
    elif opcode == 0xa1:
        instruction['name'] = "if_icmplt"
        instruction['args'] = [read_signed_16(reader)]
    elif opcode == 0xa2:
        instruction['name'] = "if_icmpge"
        instruction['args'] = [read_signed_16(reader)]
    elif opcode == 0xa3:
        instruction['name'] = "if_icmpgt"
        instruction['args'] = [read_signed_16(reader)]
    elif opcode == 0xa4:
        instruction['name'] = "if_icmple"
        instruction['args'] = [read_signed_16(reader)]
    elif opcode == 0x99:
        instruction['name'] = "ifeq"
        instruction['args'] = [read_signed_16(reader)]
    elif opcode == 0x9a:
        instruction['name'] = "ifne"
        instruction['args'] = [read_signed_16(reader)]
    elif opcode == 0x9b:
        instruction['name'] = "iflt"
        instruction['args'] = [read_signed_16(reader)]
    elif opcode == 0x9c:
        instruction['name'] = "ifge"
        instruction['args'] = [read_signed_16(reader)]
    elif opcode == 0x9d:
        instruction['name'] = "ifgt"
        instruction['args'] = [read_signed_16(reader)]
    elif opcode == 0x9e:
        instruction['name'] = "ifle"
        instruction['args'] = [read_signed_16(reader)]
    elif opcode == 0xc7:
        instruction['name'] = "ifnonnull"
        instruction['args'] = [read_signed_16(reader)]
    elif opcode == 0xc6:
        instruction['name'] = "ifnull"
        instruction['args'] = [read_signed_16(reader)]
    elif opcode == 0x84:
        instruction['name'] = "iinc"
        instruction['args'] = [read_unsigned_8(reader), read_signed_8(reader)]
    elif opcode == 0x15:
        instruction['name'] = "iload"
        instruction['args'] = [read_unsigned_8(reader)]
    elif opcode == 0x1a:
        instruction['name'] = "iload_0"
    elif opcode == 0x1b:
        instruction['name'] = "iload_1"
    elif opcode == 0x1c:
        instruction['name'] = "iload_2"
    elif opcode == 0x1d:
        instruction['name'] = "iload_3"
    elif opcode == 0x68:
        instruction['name'] = "imul"
    elif opcode == 0x74:
        instruction['name'] = "ineg"
    elif opcode == 0xc1:
        instruction['name'] = "instanceof"
        instruction['args'] = [read_signed_16(reader)]
    elif opcode == 0xba:
        instruction['name'] = "invokedynamic"
        instruction['args'] = [read_signed_16(reader), reader.read(1), reader.read(1)]
    elif opcode == 0xb9:
        instruction['name'] = "invokeinterface"
        instruction['args'] = [read_signed_16(reader), read_unsigned_8(reader), reader.read(1)]
    elif opcode == 0xb7:
        instruction['name'] = "invokespecial"
        instruction['args'] = [read_signed_16(reader)]
    elif opcode == 0xb8:
        instruction['name'] = "invokestatic"
        instruction['args'] = [read_signed_16(reader)]
    elif opcode == 0xb6:
        instruction['name'] = "invokevirtual"
        instruction['args'] = [read_signed_16(reader)]
    elif opcode == 0x80:
        instruction['name'] = "ior"
    elif opcode == 0x70:
        instruction['name'] = "irem"
    elif opcode == 0xac:
        instruction['name'] = "ireturn"
    elif opcode == 0x78:
        instruction['name'] = "ishl"
    elif opcode == 0x7a:
        instruction['name'] = "ishr"
    elif opcode == 0x36:
        instruction['name'] = "istore"
        instruction['args'] = [read_unsigned_8(reader)]
    elif opcode == 0x3b:
        instruction['name'] = "istore_0"
    elif opcode == 0x3c:
        instruction['name'] = "istore_1"
    elif opcode == 0x3d:
        instruction['name'] = "istore_2"
    elif opcode == 0x3e:
        instruction['name'] = "istore_3"
    elif opcode == 0x64:
        instruction['name'] = "isub"
    elif opcode == 0x7c:
        instruction['name'] = "iushr"
    elif opcode == 0x82:
        instruction['name'] = "ixor"
    elif opcode == 0xa8:
        instruction['name'] = "jsr"
        instruction['args'] = [read_signed_16(reader)]
    elif opcode == 0xc9:
        instruction['name'] = "jsr_w"
        instruction['args'] = [read_signed_32(reader)]
    elif opcode == 0x8a:
        instruction['name'] = "l2d"
    elif opcode == 0x89:
        instruction['name'] = "l2f"
    elif opcode == 0x88:
        instruction['name'] = "l2i"
    elif opcode == 0x61:
        instruction['name'] = "ladd"
    elif opcode == 0x2f:
        instruction['name'] = "laload"
    elif opcode == 0x7f:
        instruction['name'] = "land"
    elif opcode == 0x50:
        instruction['name'] = "lastore"
    elif opcode == 0x94:
        instruction['name'] = "lcmp"
    elif opcode == 0x9:
        instruction['name'] = "lconst_0"
    elif opcode == 0xa:
        instruction['name'] = "lconst_1"
    elif opcode == 0x12:
        instruction['name'] = "ldc"
        instruction['args'] = [read_unsigned_8(reader)]
    elif opcode == 0x13:
        instruction['name'] = "ldc_w"
        instruction['args'] = [read_unsigned_16(reader)]
    elif opcode == 0x14:
        instruction['name'] = "ldc2_w"
        instruction['args'] = [read_unsigned_16(reader)]
    elif opcode == 0x6d:
        instruction['name'] = "ldiv"
    elif opcode == 0x16:
        instruction['name'] = "lload"
        instruction['args'] = [read_unsigned_8(reader)]
    elif opcode == 0x1e:
        instruction['name'] = "lload_0"
    elif opcode == 0x1f:
        instruction['name'] = "lload_1"
    elif opcode == 0x20:
        instruction['name'] = "lload_2"
    elif opcode == 0x21:
        instruction['name'] = "lload_3"
    elif opcode == 0x69:
        instruction['name'] = "lmul"
    elif opcode == 0x75:
        instruction['name'] = "lneg"
    elif opcode == 0xab:
        instruction['name'] = "lookupswitch"
        ...
    elif opcode == 0x81:
        instruction['name'] = "lor"
    elif opcode == 0x71:
        instruction['name'] = "lrem"
    elif opcode == 0xad:
        instruction['name'] = "lreturn"
    elif opcode == 0x79:
        instruction['name'] = "lshl"
    elif opcode == 0x7b:
        instruction['name'] = "lshr"
    elif opcode == 0x37:
        instruction['name'] = "lstore"
        instruction['args'] = [read_unsigned_8(reader)]
    elif opcode == 0x3f:
        instruction['name'] = "lstore_0"
    elif opcode == 0x40:
        instruction['name'] = "lstore_1"
    elif opcode == 0x41:
        instruction['name'] = "lstore_2"
    elif opcode == 0x42:
        instruction['name'] = "lstore_3"
    elif opcode == 0x65:
        instruction['name'] = "lsub"
    elif opcode == 0x7d:
        instruction['name'] = "lushr"
    elif opcode == 0x83:
        instruction['name'] = "lxor"
    elif opcode == 0xc2:
        instruction['name'] = "monitorenter"
    elif opcode == 0xc3:
        instruction['name'] = "monitorexit"
    elif opcode == 0xc5:
        instruction['name'] = "multianewarray"
        instruction['args'] = [read_unsigned_16(reader), read_unsigned_8(reader)]
    elif opcode == 0xbb:
        instruction['name'] = "new"
        instruction['args'] = [read_unsigned_16(reader)]
    elif opcode == 0xbc:
        instruction['name'] = "newarray"
        instruction['args'] = [read_unsigned_8(reader)]
    elif opcode == 0x0:
        instruction['name'] = "nop"
    elif opcode == 0x57:
        instruction['name'] = "pop"
    elif opcode == 0x58:
        instruction['name'] = "pop2"
    elif opcode == 0xb5:
        instruction['name'] = "putfield"
        instruction['args'] = [read_unsigned_16(reader)]
    elif opcode == 0xb3:
        instruction['name'] = "putstatic"
        instruction['args'] = [read_unsigned_16(reader)]
    elif opcode == 0xa9:
        instruction['name'] = "ret"
        instruction['args'] = [read_unsigned_8(reader)]
    elif opcode == 0xb1:
        instruction['name'] = "return"
    elif opcode == 0x35:
        instruction['name'] = "saload"
    elif opcode == 0x56:
        instruction['name'] = "sastore"
    elif opcode == 0x11:
        instruction['name'] = "sipush"
        instruction['args'] = [read_signed_16(reader)]
    elif opcode == 0x5f:
        instruction['name'] = "swap"
    elif opcode == 0xaa:
        instruction['name'] = "tableswitch"
        ...
    elif opcode == 0xc4:
        instruction['name'] = "wide"
        ...

    if not instruction['name']:
        # raise
        instruction['name'] = "not found"
        instruction['args'] = opcode
        reader.read(1)

    return instruction


def read_signed_8(reader):
    return int.from_bytes(reader.read(1), "big", signed=True)


def read_unsigned_8(reader):
    return int.from_bytes(reader.read(1), "big", signed=False)


def read_signed_16(reader):
    byte1 = bytes_to_int(reader.read(1))
    byte2 = bytes_to_int(reader.read(1))
    return (byte1 << 8) | byte2


def read_unsigned_16(reader):
    byte1 = bytes_to_int(reader.read(1))
    byte2 = bytes_to_int(reader.read(1))
    return (byte1 << 8) | byte2


def read_signed_32(reader):
    byte1 = bytes_to_int(reader.read(1))
    byte2 = bytes_to_int(reader.read(1))
    byte3 = bytes_to_int(reader.read(1))
    byte4 = bytes_to_int(reader.read(1))
    return (byte1 << 24) | (byte2 << 16) | (byte3 << 8) | byte4
