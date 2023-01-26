import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    assert encrypt_message('abcde', 2) == 'edc_ba'
    assert encrypt_message('abcde', 3) == 'cba_ed'
    assert encrypt_message('abcde', 6) == 'edcba'

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message('abc', 'abc')

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(1, 9)
