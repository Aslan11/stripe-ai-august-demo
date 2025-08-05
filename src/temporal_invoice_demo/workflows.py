"""Temporal workflow scaffolding for invoice processing."""

from __future__ import annotations
from typing import Any

from .agent import InvoiceAgent
from .fraud import perform_fraud_check
from .stripe_integration import StripeClient
from .human_review import approve_invoice


async def invoice_processor(invoice: Any) -> str:
    """Main workflow for processing invoices.

    The function's body contains placeholder logic demonstrating how components
    fit together. Temporal workflow definitions will be added in the real
    implementation.
    """
    agent = InvoiceAgent()
    stripe = StripeClient()

    if not perform_fraud_check(invoice):
        return "fraud-detected"

    result = await agent.evaluate(invoice)
    if result.approved:
        stripe.finalize_invoice(invoice.id)
        return "approved"

    # Simulate waiting for human signal.
    approve_invoice(invoice.id)
    # In a real workflow the following would be triggered by a signal:
    stripe.finalize_invoice(invoice.id)
    return "approved-by-human"
