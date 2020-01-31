import unittest
from traits import trait_notifiers as trait_notifiers
from traits.api import Callable as Callable, Float as Float, HasTraits as HasTraits, on_trait_change as on_trait_change
from traitsui.qt4 import toolkit as toolkit
from typing import Any

qt4_app: Any
QT_FOUND: bool

class CalledAsMethod(HasTraits):
    foo: Any = ...

class CalledAsDecorator(HasTraits):
    foo: Any = ...
    callback: Any = ...
    def on_foo_change(self, obj: Any, name: Any, old: Any, new: Any) -> None: ...

class BaseTestUINotifiers:
    notifications: Any = ...
    def setUp(self) -> None: ...
    def flush_event_loop(self) -> None: ...
    def on_foo_notifications(self, obj: Any, name: Any, old: Any, new: Any) -> None: ...
    def test_notification_from_main_thread(self) -> None: ...
    def test_notification_from_separate_thread(self) -> None: ...

class TestMethodUINotifiers(BaseTestUINotifiers, unittest.TestCase):
    def obj_factory(self): ...

class TestDecoratorUINotifiers(BaseTestUINotifiers, unittest.TestCase):
    def obj_factory(self): ...