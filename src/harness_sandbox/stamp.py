"""What the loop smoke changes: each smoke ticket makes stamp() return its UTC stamp."""

from __future__ import annotations


def stamp() -> str:
    """The stamp of the last loop smoke run that landed, or "" before the first."""
    return "20261123T114140Z"
