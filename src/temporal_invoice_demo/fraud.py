"""Optional fraud check using Stripe Radar."""

from __future__ import annotations
from typing import Any


def perform_fraud_check(invoice: Any) -> bool:
    """Return ``True`` if invoice passes the fraud check."""
    # The real implementation would integrate with Stripe Radar. We simply
    # return ``True`` to indicate the invoice is not fraudulent.
    return True
