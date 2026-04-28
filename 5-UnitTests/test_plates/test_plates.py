import plates


def test_in_char_range():
    assert plates.is_valid("ABCD")


def test_above_char_range():
    assert plates.is_valid("ABCDEFG") == False


def test_below_characters():
    assert plates.is_valid("A") == False


def test_starts_with_numbers():
    assert plates.is_valid("12CD") == False


def test_non_alnum():
    assert plates.is_valid("!@#$") == False


def test_numbers_in_middle():
    assert plates.is_valid("A23D") == False


def test_first_number_is_0():
    assert plates.is_valid("AB04") == False
