"""AI agent placeholder using OpenAI Agents SDK."""

from __future__ import annotations
from dataclasses import dataclass
from typing import Any


@dataclass
class EvaluationResult:
    """Represents the agent's decision about an invoice."""
    approved: bool
    reason: str


class InvoiceAgent:
    """Stub for the agent responsible for invoice evaluation."""

    threshold: float = 500.0

    async def evaluate(self, invoice: Any) -> EvaluationResult:
        """Evaluate an invoice and return a decision.

        The real implementation would send invoice details to an OpenAI agent
        via Stripe's Agent Toolkit. For scaffolding we simply approve invoices
        below the ``threshold`` value.
        """
        approved = invoice.amount <= self.threshold
        reason = "auto-approved" if approved else "requires human review"
        return EvaluationResult(approved=approved, reason=reason)
