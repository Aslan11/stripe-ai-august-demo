"""Helpers for human-in-the-loop approvals using Temporal signals."""

from __future__ import annotations
from typing import Any


def approve_invoice(invoice_id: str) -> None:
    """Placeholder for signal to approve an invoice."""
    print(f"[human] approve invoice {invoice_id}")


def reject_invoice(invoice_id: str) -> None:
    """Placeholder for signal to reject an invoice."""
    print(f"[human] reject invoice {invoice_id}")
