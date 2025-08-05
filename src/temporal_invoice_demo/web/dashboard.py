"""Minimal Flask dashboard used for scaffolding."""

from __future__ import annotations
from flask import Flask


def create_app() -> Flask:
    """Return a basic Flask application."""
    app = Flask(__name__)

    @app.route("/")
    def index() -> str:  # pragma: no cover - trivial
        return "Invoice Dashboard"

    return app
