import plates


def test_in_char_range():
    assert plates.is_valid("ABCD") == True


def test_below_char_range():
    assert plates.is_valid("A") == False


def test_above_char_range():
    assert plates.is_valid("ABCDEFG") == False


def test_non_alnum():
    assert plates.is_valid("!BCD") == False


def test_first_num_0():
    assert plates.is_valid("AB01") == False


def test_alpha_after_num():
    assert plates.is_valid("A12D") == False
