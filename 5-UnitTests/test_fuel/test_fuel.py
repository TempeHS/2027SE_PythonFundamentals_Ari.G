import fuel


def test_valid_fraction():
    assert fuel.check_fuel("1/2") == "50%"


def test_zero_division():
    assert fuel.check_fuel("1/0") == "Please enter a valid fraction"


def test_non_numeric():
    assert fuel.check_fuel("A/B") == "Please enter a valid fraction"
