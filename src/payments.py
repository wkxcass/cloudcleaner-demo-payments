"""Synthetic payment-processing logic for CloudCleaner demos."""


def authorize_payment(amount_cents: int) -> bool:
    """Return whether a demo payment amount is valid for authorization."""
    if amount_cents <= 0:
        return False
    return amount_cents <= 100_000


def calculate_fee(amount_cents: int) -> int:
    """Calculate a simple 2% demo processing fee in cents."""
    if amount_cents < 0:
        raise ValueError("amount_cents must be non-negative")
    return amount_cents * 2 // 100
