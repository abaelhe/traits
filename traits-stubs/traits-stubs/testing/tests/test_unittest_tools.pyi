from traits.api import Bool as Bool, Event as Event, Float as Float, HasTraits as HasTraits, Int as Int, List as List, on_trait_change as on_trait_change
from traits.testing.api import UnittestTools as UnittestTools
from traits.testing.unittest_tools import unittest as unittest
from traits.util.api import deprecated as deprecated
from typing import Any

def old_and_dull() -> None: ...

class TestObject(HasTraits):
    number: Any = ...
    list_of_numbers: Any = ...
    flag: Any = ...
    def add_to_number(self, value: Any) -> None: ...

class UnittestToolsTestCase(unittest.TestCase, UnittestTools):
    test_object: Any = ...
    def setUp(self) -> None: ...
    def test_when_using_with(self) -> None: ...
    def test_assert_multi_changes(self) -> None: ...
    def test_when_using_functions(self) -> None: ...
    def test_indirect_events(self) -> None: ...
    def test_exception_inside_context(self) -> None: ...
    def test_non_change_on_failure(self) -> None: ...
    def test_change_on_failure(self) -> None: ...
    def test_asserts_in_context_block(self) -> None: ...
    def test_special_case_for_count(self) -> None: ...
    def test_assert_trait_changes_async(self) -> None: ...
    def test_assert_trait_changes_async_events(self) -> None: ...
    def test_assert_trait_changes_async_failure(self) -> None: ...
    def test_assert_eventually_true_fails_on_timeout(self): ...
    def test_assert_eventually_true_passes_when_condition_becomes_true(self): ...
    def test_assert_eventually_true_passes_when_condition_starts_true(self): ...
    def test_assert_deprecated(self) -> None: ...
    def test_assert_deprecated_failures(self) -> None: ...
    def test_assert_deprecated_when_warning_already_issued(self) -> None: ...
    def test_assert_not_deprecated_failures(self) -> None: ...
    def test_assert_not_deprecated(self) -> None: ...
    def test_assert_not_deprecated_when_warning_already_issued(self) -> None: ...