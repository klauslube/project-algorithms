import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    assert encrypt_message('abcde', 2) == 'edc_ba'
    assert encrypt_message('abcde', 3) == 'cde_ba'
    assert encrypt_message('abcde', 6) == 'edcba'

    with pytest.raises(TypeError, match="invalid key type"):
        encrypt_message('abc', 'abc')

    with pytest.raises(TypeError, match="invalid message type"):
        encrypt_message(1, 9)
