import unittest
from traits.api import Delegate as Delegate, HasTraits as HasTraits, Instance as Instance, Str as Str
from typing import Any

baz_s_handler_self: Any
baz_sd_handler_self: Any
baz_u_handler_self: Any
baz_t_handler_self: Any
foo_s_handler_self: Any
foo_t_handler_self: Any

class Foo(HasTraits):
    s: Any = ...
    t: Any = ...
    u: Any = ...

class Bar(HasTraits):
    foo: Any = ...
    s: Any = ...

class BazModify(HasTraits):
    foo: Any = ...
    sd: Any = ...
    t: Any = ...
    u: Any = ...

class BazNoModify(HasTraits):
    foo: Any = ...
    sd: Any = ...
    t: Any = ...
    u: Any = ...

class DelegateTestCase(unittest.TestCase):
    def setUp(self) -> None: ...
    def test_reset(self) -> None: ...
    def test_modify_prefix_handler_on_delegator(self) -> None: ...
    def test_modify_prefix_handler_on_delegatee(self) -> None: ...
    def test_no_modify_prefix_handler_on_delegator(self) -> None: ...
    def test_no_modify_prefix_handler_on_delegatee_not_called(self) -> None: ...
    def test_modify_handler_on_delegator(self) -> None: ...
    def test_modify_handler_on_delegatee(self) -> None: ...
    def test_no_modify_handler_on_delegator(self) -> None: ...
    def test_no_modify_handler_on_delegatee_not_called(self) -> None: ...
    def test_no_modify_handler_on_delegatee_direct_change(self) -> None: ...
    def test_no_modify_handler_on_delegator_direct_change(self) -> None: ...
    def test_modify_handler_on_delegatee_direct_change(self) -> None: ...
    def test_modify_handler_on_delegator_direct_change(self) -> None: ...
    def test_modify_handler_not_listenable(self) -> None: ...
    def test_no_modify_handler_not_listenable(self) -> None: ...