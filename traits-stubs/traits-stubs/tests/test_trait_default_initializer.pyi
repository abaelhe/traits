import unittest
from traits.has_traits import HasTraits as HasTraits
from traits.trait_types import Int as Int
from typing import Any

class Foo(HasTraits):
    bar: Any = ...

class TestTraitDefaultInitializer(unittest.TestCase):
    def test_default_value(self) -> None: ...
    def test_default_value_override(self) -> None: ...
    def test_reset_to_default(self) -> None: ...
    def test_error_propagation_in_default_methods(self): ...