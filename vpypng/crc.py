from zlib import crc32

def calculate_crc(data: bytes) -> int:
    if not isinstance(data, bytes):
        data=bytes(data)

    return crc32(data)


def check_crc_is_same(data: bytes, crc: int) -> bool:
    if not isinstance(data, bytes):
        data=bytes(data)

    return crc32(data) == crc