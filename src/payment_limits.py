"""Demo validation rules added on a feature branch."""

MAX_SINGLE_PAYMENT_CENTS = 100_000


def within_demo_limit(amount_cents: int) -> bool:
    return 0 < amount_cents <= MAX_SINGLE_PAYMENT_CENTS
