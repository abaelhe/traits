import unittest
from traits import has_traits as has_traits
from traits.adaptation.api import reset_global_adaptation_manager as reset_global_adaptation_manager
from traits.api import Adapter as Adapter, HasTraits as HasTraits, Instance as Instance, Int as Int, Interface as Interface, provides as provides, register_factory as register_factory
from traits.interface_checker import InterfaceError as InterfaceError, check_implements as check_implements

class InterfaceCheckerTestCase(unittest.TestCase):
    def setUp(self) -> None: ...
    def test_non_traits_class(self) -> None: ...
    def test_single_interface(self) -> None: ...
    def test_single_interface_with_invalid_method_signature(self) -> None: ...
    def test_single_interface_with_missing_trait(self) -> None: ...
    def test_single_interface_with_missing_method(self) -> None: ...
    def test_multiple_interfaces(self) -> None: ...
    def test_multiple_interfaces_with_invalid_method_signature(self) -> None: ...
    def test_multiple_interfaces_with_missing_trait(self) -> None: ...
    def test_multiple_interfaces_with_missing_method(self) -> None: ...
    def test_inherited_interfaces(self) -> None: ...
    def test_inherited_interfaces_with_invalid_method_signature(self) -> None: ...
    def test_inherited_interfaces_with_missing_trait(self) -> None: ...
    def test_inherited_interfaces_with_missing_method(self) -> None: ...
    def test_subclasses_with_wrong_signature_methods(self) -> None: ...
    def test_instance(self) -> None: ...
    def test_callable(self) -> None: ...
    def test_adaptation(self) -> None: ...