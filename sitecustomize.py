"""Compatibility shim for legacy nose on Python 3.10+."""

import collections
import collections.abc

if not hasattr(collections, "Callable"):
    collections.Callable = collections.abc.Callable
