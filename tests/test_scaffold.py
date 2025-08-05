"""Basic tests ensuring scaffold imports correctly."""

import asyncio

from temporal_invoice_demo.invoice_service import generate_invoice
from temporal_invoice_demo.agent import InvoiceAgent


def test_invoice_generation_and_agent_evaluation():
    invoice = generate_invoice(100, "demo")
    agent = InvoiceAgent()
    result = asyncio.run(agent.evaluate(invoice))
    assert result.approved
