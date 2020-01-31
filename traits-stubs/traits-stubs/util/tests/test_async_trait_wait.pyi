import unittest
from traits.api import Enum as Enum, HasStrictTraits as HasStrictTraits
from traits.util.async_trait_wait import wait_for_condition as wait_for_condition
from typing import Any

class TrafficLights(HasStrictTraits):
    colour: Any = ...
    def make_random_changes(self, change_count: Any) -> None: ...

class TestAsyncTraitWait(unittest.TestCase):
    def test_wait_for_condition_success(self): ...
    def test_wait_for_condition_failure(self): ...
    lights: Any = ...
    def test_traits_handler_cleaned_up(self): ...
