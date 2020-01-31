import unittest
from traits.api import Float as Float, HasTraits as HasTraits, Int as Int, List as List
from typing import Any

class Foo(HasTraits):
    x: Any = ...
    y_changes: Any = ...

class TestDynamicTraitDefinition(unittest.TestCase):
    def test_add_trait(self) -> None: ...
    def test_remove_trait(self) -> None: ...