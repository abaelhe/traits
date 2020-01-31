import unittest
from traits.api import Any as Any, HasTraits as HasTraits, Instance as Instance, Str as Str

class TestEventOrder(unittest.TestCase):
    events_delivered: Any = ...
    def test_lifo_order(self) -> None: ...

class Foo(HasTraits):
    cause: Any = ...

class Bar(HasTraits):
    foo: Any = ...
    effect: Any = ...
    test: Any = ...

class Baz(HasTraits):
    bar: Any = ...
    test: Any = ...