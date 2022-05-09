"""Top-level package for straydoc."""

__author__ = """lot_carnage"""
__email__ = 'lotcarnage@gmail.com'
__version__ = '0.1.0'

from .straydoc import create_markdown_ast
from .straydoc import to_latex


__all__ = [
    'create_markdown_ast',
    'to_latex'
]
