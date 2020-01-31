import unittest
from traits.api import Any as Any, Bytes as Bytes, CBytes as CBytes, CFloat as CFloat, CInt as CInt, ComparisonMode as ComparisonMode, Delegate as Delegate, Float as Float, HasTraits as HasTraits, Instance as Instance, Int as Int, List as List, Range as Range, Str as Str, This as This, Trait as Trait, TraitError as TraitError, TraitList as TraitList, TraitPrefixList as TraitPrefixList, TraitPrefixMap as TraitPrefixMap, Tuple as Tuple, pop_exception_handler as pop_exception_handler, push_exception_handler as push_exception_handler
from typing import Optional

class BaseTest:
    def assign(self, value: Any) -> None: ...
    def coerce(self, value: Any): ...
    def test_assignment(self) -> None: ...

class test_base2(unittest.TestCase):
    def indexed_assign(self, list: Any, index: Any, value: Any) -> None: ...
    def indexed_range_assign(self, list: Any, index1: Any, index2: Any, value: Any) -> None: ...
    def extended_slice_assign(self, list: Any, index1: Any, index2: Any, step: Any, value: Any) -> None: ...
    def check_values(self, name: Any, default_value: Any, good_values: Any, bad_values: Any, actual_values: Optional[Any] = ..., mapped_values: Optional[Any] = ...) -> None: ...

class AnyTrait(HasTraits):
    value: Any = ...

class AnyTraitTest(BaseTest, unittest.TestCase):
    obj: Any = ...
    def setUp(self) -> None: ...

class CoercibleIntTrait(HasTraits):
    value: Any = ...

class IntTrait(HasTraits):
    value: Any = ...

class CoercibleIntTest(AnyTraitTest):
    obj: Any = ...
    def setUp(self) -> None: ...
    def coerce(self, value: Any): ...

class IntTest(AnyTraitTest):
    obj: Any = ...
    def setUp(self) -> None: ...
    def coerce(self, value: Any): ...

class CoercibleFloatTrait(HasTraits):
    value: Any = ...

class FloatTrait(HasTraits):
    value: Any = ...

class CoercibleFloatTest(AnyTraitTest):
    obj: Any = ...
    def setUp(self) -> None: ...
    def coerce(self, value: Any): ...

class FloatTest(AnyTraitTest):
    obj: Any = ...
    def setUp(self) -> None: ...
    def coerce(self, value: Any): ...

class ImaginaryValueTrait(HasTraits):
    value: Any = ...

class ImaginaryValueTest(AnyTraitTest):
    obj: Any = ...
    def setUp(self) -> None: ...
    def coerce(self, value: Any): ...

class StringTrait(HasTraits):
    value: Any = ...

class StringTest(AnyTraitTest):
    obj: Any = ...
    def setUp(self) -> None: ...
    def coerce(self, value: Any): ...

class BytesTrait(HasTraits):
    value: Any = ...

class BytesTest(StringTest):
    obj: Any = ...
    def setUp(self) -> None: ...
    def coerce(self, value: Any): ...

class CoercibleBytesTrait(HasTraits):
    value: Any = ...

class CoercibleBytesTest(StringTest):
    obj: Any = ...
    def setUp(self) -> None: ...
    def coerce(self, value: Any): ...

class EnumTrait(HasTraits):
    value: Any = ...

class EnumTest(AnyTraitTest):
    obj: Any = ...
    def setUp(self) -> None: ...

class MappedTrait(HasTraits):
    value: Any = ...

class MappedTest(AnyTraitTest):
    obj: Any = ...
    def setUp(self) -> None: ...

class PrefixListTrait(HasTraits):
    value: Any = ...

class PrefixListTest(AnyTraitTest):
    obj: Any = ...
    def setUp(self) -> None: ...
    def coerce(self, value: Any): ...

class PrefixMapTrait(HasTraits):
    value: Any = ...

class PrefixMapTest(AnyTraitTest):
    obj: Any = ...
    def setUp(self) -> None: ...
    def coerce(self, value: Any): ...

class OTraitTest1: ...
class OTraitTest2(OTraitTest1): ...
class OTraitTest3(OTraitTest2): ...
class OBadTraitTest: ...

otrait_test1: Any

class OldInstanceTrait(HasTraits):
    value: Any = ...

class OldInstanceTest(AnyTraitTest):
    obj: Any = ...
    def setUp(self) -> None: ...

class NTraitTest1: ...
class NTraitTest2(NTraitTest1): ...
class NTraitTest3(NTraitTest2): ...
class NBadTraitTest: ...

ntrait_test1: Any

class NewInstanceTrait(HasTraits):
    value: Any = ...

class NewInstanceTest(AnyTraitTest):
    obj: Any = ...
    def setUp(self) -> None: ...

class FactoryClass(HasTraits): ...

class ConsumerClass(HasTraits):
    x: Any = ...

class ConsumerSubclass(ConsumerClass):
    x: Any = ...

embedded_instance_trait: Any

class Dummy(HasTraits):
    x: Any = ...
    xl: Any = ...

class RegressionTest(unittest.TestCase):
    def test_factory_subclass_no_segfault(self) -> None: ...
    def test_trait_compound_instance(self) -> None: ...

def odd_integer(object: Any, name: Any, value: Any): ...

class OddIntegerTrait(HasTraits):
    value: Any = ...

class OddIntegerTest(AnyTraitTest):
    obj: Any = ...
    def setUp(self) -> None: ...

class NotifierTraits(HasTraits):
    value1: Any = ...
    value2: Any = ...
    value1_count: Any = ...
    value2_count: Any = ...

class NotifierTests(unittest.TestCase):
    def setUp(self) -> None: ...
    def tearDown(self) -> None: ...
    def on_anytrait_changed(self, object: Any, trait_name: Any, old: Any, new: Any) -> None: ...
    def on_value1_changed(self) -> None: ...
    def on_value2_changed(self) -> None: ...
    def test_simple(self) -> None: ...
    def test_complex(self) -> None: ...

class RaisesArgumentlessRuntimeError(HasTraits):
    x: Any = ...

class TestRuntimeError(unittest.TestCase):
    def setUp(self) -> None: ...
    def tearDown(self) -> None: ...
    def test_runtime_error(self) -> None: ...

class DelegatedFloatTrait(HasTraits):
    value: Any = ...

class DelegateTrait(HasTraits):
    value: Any = ...
    delegate: Any = ...

class DelegateTrait2(DelegateTrait):
    delegate: Any = ...

class DelegateTrait3(DelegateTrait):
    delegate: Any = ...

class DelegateTests(unittest.TestCase):
    def test_delegation(self) -> None: ...

slow: Any

class complex_value(HasTraits):
    num1: Any = ...
    num2: Any = ...
    num3: Any = ...
    num4: Any = ...
    num5: Any = ...

class test_complex_value(test_base2):
    obj: Any = ...
    def setUp(self) -> None: ...
    def test_num1(self) -> None: ...
    def test_enum_exceptions(self) -> None: ...

class test_list_value(test_base2):
    obj: Any = ...
    last_event: Any = ...
    def setUp(self) -> None: ...
    def tearDown(self) -> None: ...
    def del_range(self, list: Any, index1: Any, index2: Any) -> None: ...
    def del_extended_slice(self, list: Any, index1: Any, index2: Any, step: Any) -> None: ...
    def check_list(self, list: Any) -> None: ...
    def test_list1(self) -> None: ...
    def test_list2(self) -> None: ...
    def assertLastTraitListEventEqual(self, index: Any, removed: Any, added: Any) -> None: ...
    def test_trait_list_event(self) -> None: ...

class ThisDummy(HasTraits):
    allows_none: Any = ...
    disallows_none: Any = ...

class TestThis(unittest.TestCase):
    def test_this_none(self) -> None: ...
    def test_this_other_class(self) -> None: ...

class ComparisonModeTests(unittest.TestCase):
    def test_comparison_mode_none(self): ...
    def test_comparison_mode_identity(self): ...
    def test_comparison_mode_equality(self): ...
    def test_rich_compare_false(self): ...
    def test_rich_compare_true(self): ...
