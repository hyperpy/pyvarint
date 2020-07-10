"""Varint encode and decode"""

from io import BytesIO


def encode(number: int) -> bytes:
    """Encode to varint

    :param number: the integer to encode
    """
    buf = b""

    while True:
        towrite = number & 0x7F
        number >>= 7
        if number:
            buf += bytes((towrite | 0x80,))
        else:
            buf += bytes((towrite,))
            break

    return buf


def decode(buf: bytes) -> int:
    """Decode to bytes

    :param buf: the buffer to decode to an integer
    """
    stream = BytesIO(buf)

    shift = 0
    result = 0

    while True:
        single_byte = stream.read(1)

        if single_byte == b"":
            raise EOFError("Unexpected EOF while reading bytes")
        ord_int = ord(single_byte)

        result |= (ord_int & 0x7F) << shift
        shift += 7

        if not (ord_int & 0x80):
            break

    return result


def encoding_length(n: int) -> int:
    """The number of bytes this number will be encoded as.

    :param n: the number for which the encoding length will be calculated
    """
    N1 = pow(2, 7)
    N2 = pow(2, 14)
    N3 = pow(2, 21)
    N4 = pow(2, 28)
    N5 = pow(2, 35)
    N6 = pow(2, 42)
    N7 = pow(2, 49)
    N8 = pow(2, 56)
    N9 = pow(2, 63)

    if n < N1:
        return 1
    elif n < N2:
        return 2
    elif n < N3:
        return 3
    elif n < N4:
        return 4
    elif n < N5:
        return 5
    elif n < N6:
        return 6
    elif n < N7:
        return 7
    elif n < N8:
        return 8
    elif n < N9:
        return 9
    else:
        return 10
