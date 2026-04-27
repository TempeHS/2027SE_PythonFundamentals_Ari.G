import twttr


def test_lowercase():
    assert twttr.shorten("abcdefghijklmnopqrstuvwxyz") == "bcdfghjklmnpqrstvwxyz"


def test_uppercase():
    assert twttr.shorten("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == "BCDFGHJKLMNPQRSTVWXYZ"


def test_numbers():
    assert twttr.shorten("1234567890") == "1234567890"


def test_non_alnum():
    assert twttr.shorten("!@#$%^&*()") == "!@#$%^&*()"
