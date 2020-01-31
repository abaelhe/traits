import unittest
from traits.api import BaseFloat as BaseFloat, Either as Either, Float as Float, HasTraits as HasTraits, Str as Str, TraitError as TraitError
from traits.testing.optional_dependencies import numpy as numpy, requires_numpy as requires_numpy
from typing import Any

class MyFloat:
    def __init__(self, value: Any) -> None: ...
    def __float__(self): ...

class InheritsFromFloat(float): ...

class BadFloat:
    def __float__(self) -> None: ...

class FloatModel(HasTraits):
    value: Any = ...
    value_or_none: Any = ...
    float_or_text: Any = ...

class BaseFloatModel(HasTraits):
    value: Any = ...
    value_or_none: Any = ...
    float_or_text: Any = ...

class CommonFloatTests:
    def test_default(self) -> None: ...
    def test_accepts_float(self) -> None: ...
    def test_accepts_float_subclass(self) -> None: ...
    def test_accepts_int(self) -> None: ...
    def test_accepts_float_like(self) -> None: ...
    def test_rejects_string(self) -> None: ...
    def test_bad_float_exceptions_propagated(self) -> None: ...
    def test_compound_trait_float_conversion_fail(self) -> None: ...
    def test_accepts_small_integer(self) -> None: ...
    def test_accepts_large_integer(self) -> None: ...
    def test_accepts_numpy_floats(self) -> None: ...

class TestFloat(unittest.TestCase, CommonFloatTests):
    test_class: Any = ...
    def setUp(self) -> None: ...
    def test_exceptions_propagate_in_compound_trait(self) -> None: ...

class TestBaseFloat(unittest.TestCase, CommonFloatTests):
    test_class: Any = ...
    def setUp(self) -> None: ...