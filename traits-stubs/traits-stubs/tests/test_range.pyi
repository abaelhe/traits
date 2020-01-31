import unittest
from traits.api import HasTraits as HasTraits, Int as Int, Range as Range, Str as Str, TraitError as TraitError
from typing import Any

class WithFloatRange(HasTraits):
    r: Any = ...
    r_copied_on_change: Any = ...

class WithLargeIntRange(HasTraits):
    r: Any = ...
    r_copied_on_change: Any = ...

class WithDynamicRange(HasTraits):
    low: Any = ...
    high: Any = ...
    value: Any = ...
    r: Any = ...

class RangeTestCase(unittest.TestCase):
    def test_non_ui_events(self) -> None: ...
    def test_non_ui_int_events(self) -> None: ...
    def test_dynamic_events(self) -> None: ...
