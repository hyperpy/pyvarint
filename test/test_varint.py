from math import floor, pow
from random import sample

from pyvarint import decode, encode, encoding_length


def test_fuzz_test():
    ten_rand_ints = sample(range(100), 10)
    for rand_int in ten_rand_ints:
        encoded = encode(rand_int)
        decoded = decode(encoded)
        assert decoded == rand_int


def test_encoding_length():
    for idx in range(0, 53):
        number = floor(pow(2, idx))
        assert len(encode(number)) == encoding_length(number)
