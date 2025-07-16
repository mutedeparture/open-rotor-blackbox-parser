def read_signed_varint(f):
    """
    Reads a signed variable-length integer from the given binary file-like object.
    Uses LEB128 zig-zag decoding as used in Betaflight logs.
    """
    result = 0
    shift = 0
    while True:
        b = f.read(1)
        if not b:
            return None
        byte = b[0]
        result |= (byte & 0x7F) << shift
        if not (byte & 0x80):
            break
        shift += 7
    return (result >> 1) ^ -(result & 1)