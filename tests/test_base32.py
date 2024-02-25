import pytest
from typeid.base32 import decode, encode


def test_encode_decode_logic() -> None:
    original_data = list(range(0, 16))

    encoded_data = encode(original_data)

    assert isinstance(encoded_data, str)

    assert encoded_data == "00041061050r3gg28a1c60t3gf"

    decoded_data = decode(encoded_data)

    assert decoded_data == original_data

@pytest.mark.parametrize("value", (b"1" * 15, b"1" * 17, b""))
def test_encode_errors(value) -> None:
    
    with pytest.raises(RuntimeError):
        encoded_data = encode(value)

@pytest.mark.parametrize("value", ("00041061050r3gg28a1c60t3gf1", "123", "1"))
def test_encode_errors(value) -> None:
    
    with pytest.raises(RuntimeError):
        encoded_data = encode(value)
        
