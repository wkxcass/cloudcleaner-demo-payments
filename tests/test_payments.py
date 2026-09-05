from src.payments import authorize_payment, calculate_fee


def test_authorize_positive_payment():
    assert authorize_payment(2500) is True


def test_reject_non_positive_payment():
    assert authorize_payment(0) is False


def test_calculate_fee():
    assert calculate_fee(2500) == 50
