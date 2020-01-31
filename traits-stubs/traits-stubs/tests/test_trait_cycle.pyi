import unittest
from traits.api import Any as Any, DelegatesTo as DelegatesTo, HasTraits as HasTraits, Instance as Instance, Int as Int

class TestCase(unittest.TestCase):
    child: Any = ...
    def test_simple_cycle_oldstyle_class(self) -> None: ...
    def test_simple_cycle_newstyle_class(self) -> None: ...
    def test_simple_cycle_hastraits(self) -> None: ...
    def test_reference_to_trait_dict(self) -> None: ...
    def test_delegates_to(self) -> None: ...