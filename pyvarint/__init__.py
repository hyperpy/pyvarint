"""pyvarint module."""

from pyvarint.varint import decode, encode, encoding_length  # noqa

__all__ = ["encode", "decode", "encoding_length"]

try:
    import pkg_resources
except ImportError:
    pass


try:
    __version__ = pkg_resources.get_distribution("pyvarint").version
except Exception:
    __version__ = "unknown"
