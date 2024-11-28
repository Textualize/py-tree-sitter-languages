"""
Binary wheels for tree-sitter for several common languages.
Does not support tree-sitter v0.22.0 and above.
"""

from tree_sitter_languages.core import get_language, get_parser

__all__ = ["get_language", "get_parser"]
