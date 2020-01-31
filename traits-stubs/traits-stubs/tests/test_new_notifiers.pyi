import unittest
from traits.api import Float as Float, HasTraits as HasTraits, List as List
from traits.testing.unittest_tools import UnittestTools as UnittestTools
from typing import Any

SAFETY_TIMEOUT: float

class RememberThreads:
    def __init__(self) -> None: ...
    def __call__(self, *args: Any, **kwargs: Any): ...
    def __enter__(self): ...
    def __exit__(self, *exc_args: Any) -> None: ...

class Foo(HasTraits):
    foo: Any = ...

class Receiver(HasTraits):
    notifications: Any = ...
    def notified(self): ...

class TestNewNotifiers(UnittestTools, unittest.TestCase):
    def test_notification_on_separate_thread(self) -> None: ...
