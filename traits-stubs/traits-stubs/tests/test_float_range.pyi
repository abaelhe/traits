import unittest
from traits.api import BaseRange as BaseRange, Either as Either, HasTraits as HasTraits, Instance as Instance, Range as Range, TraitError as TraitError
from traits.testing.optional_dependencies import numpy as numpy, requires_numpy as requires_numpy
from typing import Any

class Impossible:
    def __init__(self) -> None: ...

def ModelFactory(name: Any, RangeFactory: Any): ...

impossible: Any

def RangeCompound(*args: Any, **kwargs: Any): ...
def BaseRangeCompound(*args: Any, **kwargs: Any): ...

ModelWithRange: Any
ModelWithBaseRange: Any
ModelWithRangeCompound: Any
ModelWithBaseRangeCompound: Any

class InheritsFromFloat(float): ...

class FloatLike:
    def __init__(self, value: Any) -> None: ...
    def __float__(self): ...

class BadFloatLike:
    def __float__(self) -> None: ...

class CommonRangeTests:
    def test_accepts_float(self) -> None: ...
    def test_accepts_int(self) -> None: ...
    def test_accepts_bool(self) -> None: ...
    def test_rejects_bad_types(self) -> None: ...
    def test_accepts_numpy_types(self) -> None: ...
    def test_accepts_float_subclass(self) -> None: ...
    def test_accepts_float_like(self) -> None: ...
    def test_bad_float_like(self) -> None: ...
    def test_endpoints(self) -> None: ...
    def test_half_infinite(self) -> None: ...

class TestFloatRange(CommonRangeTests, unittest.TestCase):
    model: Any = ...
    def setUp(self) -> None: ...

class TestFloatBaseRange(CommonRangeTests, unittest.TestCase):
    model: Any = ...
    def setUp(self) -> None: ...

class TestFloatRangeCompound(CommonRangeTests, unittest.TestCase):
    model: Any = ...
    def setUp(self) -> None: ...

class TestFloatBaseRangeCompound(CommonRangeTests, unittest.TestCase):
    model: Any = ...
    def setUp(self) -> None: ...
