import unittest
from traits.adaptation.api import AdaptationManager as AdaptationManager
from typing import Any

class TestAdaptationManagerWithABC(unittest.TestCase):
    examples: Any = ...
    adaptation_manager: Any = ...
    def setUp(self) -> None: ...
    def tearDown(self) -> None: ...
    def test_no_adapter_required(self) -> None: ...
    def test_no_adapter_available(self) -> None: ...
    def test_one_step_adaptation(self) -> None: ...
    def test_adapter_chaining(self) -> None: ...
    def test_multiple_paths_unambiguous(self) -> None: ...
    def test_multiple_paths_ambiguous(self) -> None: ...
    def test_conditional_adaptation(self): ...
    def test_spillover_adaptation_behavior(self) -> None: ...
    def test_adaptation_prefers_subclasses(self) -> None: ...
    def test_adaptation_prefers_subclasses_other_registration_order(self) -> None: ...
    def test_circular_adaptation(self): ...
    def test_default_argument_in_adapt(self) -> None: ...
    def test_prefer_specific_interfaces(self) -> None: ...
    def test_chaining_with_intermediate_mro_climbing(self) -> None: ...
    allow_adaptation: Any = ...
    def test_conditional_recycling(self): ...
    def test_provides_protocol_for_interface_subclass(self) -> None: ...
    def test_register_provides(self) -> None: ...
