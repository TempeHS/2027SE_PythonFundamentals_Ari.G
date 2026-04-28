import bank


def test_hello():
    assert bank.value("hello") == 100


def test_hello_uppercase():
    assert bank.value("HELLO") == 100


def test_starts_with_h():
    assert bank.value("habcd") == 20


def test_starts_with_h_uppercase():
    assert bank.value("HABCD") == 20


def test_contains_h():
    assert bank.value("abhcd") == 0


def test_contains_h_uppercase():
    assert bank.value("ABHCD") == 0
