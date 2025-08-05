"""Integration helpers for Stripe's Invoice API."""

from __future__ import annotations
from typing import Any


class StripeClient:
    """Very small facade around Stripe API interactions."""

    def create_invoice(self, invoice: Any) -> None:
        """Create an invoice in Stripe.

        The real implementation would call Stripe's API. The scaffolding version
        only logs the intent.
        """
        print(f"[stripe] create invoice {invoice.id}")

    def finalize_invoice(self, invoice_id: str) -> None:
        """Finalize an invoice in Stripe."""
        print(f"[stripe] finalize invoice {invoice_id}")

    def cancel_invoice(self, invoice_id: str) -> None:
        """Cancel an invoice in Stripe."""
        print(f"[stripe] cancel invoice {invoice_id}")
