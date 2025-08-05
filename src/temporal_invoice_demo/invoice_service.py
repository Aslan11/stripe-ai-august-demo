"""Invoice generation service stubs."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class Invoice:
    """Simple invoice data model used for scaffolding."""
    id: str
    amount: float
    description: str


def generate_invoice(amount: float, description: str) -> Invoice:
    """Return a dummy invoice instance.

    In the real system this would interface with Stripe to create an invoice or
    pull one from a data source. For scaffolding we simply return an ``Invoice``
    object with a generated identifier.
    """
    identifier = "INV-000"
    return Invoice(id=identifier, amount=amount, description=description)
