import unittest
from traits.api import CInt as CInt, Either as Either, HasTraits as HasTraits, Int as Int, TraitError as TraitError
from traits.testing.optional_dependencies import numpy as numpy, requires_numpy as requires_numpy
from typing import Any

class A(HasTraits):
    integral: Any = ...
    convertible: Any = ...
    convertible_or_none: Any = ...

class IntegerLike:
    def __index__(self): ...

class Truncatable:
    def __int__(self): ...

class TestInt(unittest.TestCase):
    def test_default(self) -> None: ...
    def test_accepts_int(self) -> None: ...
    def test_accepts_large_integer(self) -> None: ...
    def test_accepts_bool(self) -> None: ...
    def test_respects_dunder_index(self) -> None: ...
    def test_rejects_dunder_int(self) -> None: ...
    def test_rejects_floating_point_types(self) -> None: ...
    def test_rejects_string(self) -> None: ...
    def test_numpy_types(self) -> None: ...
    def test_cint_conversion_of_subclasses(self) -> None: ...