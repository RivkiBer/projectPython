# Package initializer for wit
# Expose the CLI entry point so `python -m wit` and entry_points work
from .wit import cli

__all__ = ["cli"]

