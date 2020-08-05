# pyvarint

[![Build Status](https://drone.autonomic.zone/api/badges/hyperpy/pyvarint/status.svg)](https://drone.autonomic.zone/hyperpy/pyvarint)

## Varints, a method of serializing integers using one or more bytes

> Generally in Python, integers are stored as long meaning that they will use
> at least 32 bits. When storing many numbers which do not require 32 bits,
> this would seem to be significantly wasteful; variable length representation
> should be able to assist in such cases.

## Install

```sh
$ pip install pyvarint
```

## Example

```python
from pyvarint import decode, encode

encoded = encode(666)
decoded = decode(encoded)

print("number: 666", f"encoded: {encoded}", f"decoded: {decoded}", sep="\n")
```

Output:

```sh
number: 666
encoded: b'\x9a\x05'
decoded: 666
```
