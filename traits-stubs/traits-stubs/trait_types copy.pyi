from .constants import DefaultValue as DefaultValue, TraitKind as TraitKind, ValidateTrait as ValidateTrait
from .editor_factories import code_editor as code_editor, date_editor as date_editor, datetime_editor as datetime_editor, html_editor as html_editor, list_editor as list_editor, password_editor as password_editor, shell_editor as shell_editor, time_editor as time_editor
from .trait_base import EnumTypes as EnumTypes, HandleWeakRef as HandleWeakRef, RangeTypes as RangeTypes, SequenceTypes as SequenceTypes, TraitsCache as TraitsCache, TypeTypes as TypeTypes, Undefined as Undefined, class_of as class_of, enum_default as enum_default, get_module_name as get_module_name, safe_contains as safe_contains, strx as strx, xgetattr as xgetattr
from .trait_converters import trait_from as trait_from
from .trait_dict_object import TraitDictEvent as TraitDictEvent, TraitDictObject as TraitDictObject
from .trait_errors import TraitError as TraitError
from .trait_list_object import TraitListEvent as TraitListEvent, TraitListObject as TraitListObject
from .trait_set_object import TraitSetEvent as TraitSetEvent, TraitSetObject as TraitSetObject
from .trait_type import TraitType as TraitType
from .traits import Trait as Trait
from .util.import_symbol import import_symbol as import_symbol
from typing import Any as _Any, Optional

MutableTypes: _Any
SetTypes: _Any
int_fast_validate: _Any
float_fast_validate: _Any
complex_fast_validate: _Any
bool_fast_validate: _Any

def default_text_editor(trait: _Any, type: Optional[_Any] = ...): ...

class Any(TraitType):
    default_value: _Any = ...
    info_text: str = ...

class BaseInt(TraitType):
    evaluate: _Any = ...
    default_value: int = ...
    info_text: str = ...
    def validate(self, object: _Any, name: _Any, value: _Any): ...
    def create_editor(self): ...

class Int(BaseInt):
    fast_validate: _Any = ...

class BaseFloat(TraitType):
    evaluate: _Any = ...
    default_value: float = ...
    info_text: str = ...
    def validate(self, object: _Any, name: _Any, value: _Any): ...
    def create_editor(self): ...

class Float(BaseFloat):
    fast_validate: _Any = ...

class BaseComplex(TraitType):
    evaluate: _Any = ...
    default_value: _Any = ...
    info_text: str = ...
    def validate(self, object: _Any, name: _Any, value: _Any): ...
    def create_editor(self): ...

class Complex(BaseComplex):
    fast_validate: _Any = ...

class BaseStr(TraitType):
    default_value: str = ...
    info_text: str = ...
    def validate(self, object: _Any, name: _Any, value: _Any): ...
    def create_editor(self): ...

class Str(BaseStr):
    fast_validate: _Any = ...

class Title(Str):
    def create_editor(self): ...

class BaseBytes(TraitType):
    default_value: bytes = ...
    info_text: str = ...
    encoding: _Any = ...
    def validate(self, object: _Any, name: _Any, value: _Any): ...
    def create_editor(self): ...

class Bytes(BaseBytes):
    fast_validate: _Any = ...

class BaseBool(TraitType):
    evaluate: _Any = ...
    default_value: bool = ...
    info_text: str = ...
    def validate(self, object: _Any, name: _Any, value: _Any): ...
    def create_editor(self): ...

class Bool(BaseBool):
    fast_validate: _Any = ...

class BaseCInt(BaseInt):
    evaluate: _Any = ...
    def validate(self, object: _Any, name: _Any, value: _Any): ...

class CInt(BaseCInt):
    fast_validate: _Any = ...

class BaseCFloat(BaseFloat):
    evaluate: _Any = ...
    def validate(self, object: _Any, name: _Any, value: _Any): ...

class CFloat(BaseCFloat):
    fast_validate: _Any = ...

class BaseCComplex(BaseComplex):
    evaluate: _Any = ...
    def validate(self, object: _Any, name: _Any, value: _Any): ...

class CComplex(BaseCComplex):
    fast_validate: _Any = ...

class BaseCStr(BaseStr):
    def validate(self, object: _Any, name: _Any, value: _Any): ...

class CStr(BaseCStr):
    fast_validate: _Any = ...

class BaseCBytes(BaseBytes):
    def validate(self, object: _Any, name: _Any, value: _Any): ...

class CBytes(BaseCBytes):
    fast_validate: _Any = ...

class BaseCBool(BaseBool):
    evaluate: _Any = ...
    def validate(self, object: _Any, name: _Any, value: _Any): ...

class CBool(BaseCBool):
    fast_validate: _Any = ...

class String(TraitType):
    minlen: _Any = ...
    maxlen: _Any = ...
    regex: _Any = ...
    def __init__(self, value: str = ..., minlen: int = ..., maxlen: _Any = ..., regex: str = ..., **metadata: _Any) -> None: ...
    def validate(self, object: _Any, name: _Any, value: _Any): ...
    def validate_all(self, object: _Any, name: _Any, value: _Any): ...
    def validate_str(self, object: _Any, name: _Any, value: _Any): ...
    def validate_len(self, object: _Any, name: _Any, value: _Any): ...
    def validate_regex(self, object: _Any, name: _Any, value: _Any): ...
    def info(self): ...
    def create_editor(self): ...

class Regex(String):
    def __init__(self, value: str = ..., regex: str = ..., **metadata: _Any) -> None: ...

class Code(String):
    metadata: _Any = ...

class HTML(String):
    metadata: _Any = ...

class Password(String):
    metadata: _Any = ...

class BaseCallable(TraitType):
    metadata: _Any = ...
    default_value: _Any = ...
    info_text: str = ...
    def validate(self, object: _Any, name: _Any, value: _Any): ...

class Callable(BaseCallable):
    fast_validate: _Any = ...

class BaseType(TraitType):
    def validate(self, object: _Any, name: _Any, value: _Any): ...

class This(BaseType):
    fast_validate: _Any = ...
    info_text: str = ...
    def __init__(self, value: Optional[_Any] = ..., allow_none: bool = ..., **metadata: _Any) -> None: ...
    def validate(self, object: _Any, name: _Any, value: _Any): ...
    def validate_none(self, object: _Any, name: _Any, value: _Any): ...
    def info(self): ...
    def info_none(self): ...

class self(This):
    default_value_type: _Any = ...

class Function(TraitType):
    fast_validate: _Any = ...
    info_text: str = ...

class Method(TraitType):
    fast_validate: _Any = ...
    info_text: str = ...

class Module(TraitType):
    fast_validate: _Any = ...
    info_text: str = ...

class Python(TraitType):
    metadata: _Any = ...
    default_value: _Any = ...

class ReadOnly(TraitType):
    ctrait_type: _Any = ...
    default_value: _Any = ...

class Disallow(TraitType):
    ctrait_type: _Any = ...

class Constant(TraitType):
    ctrait_type: _Any = ...
    metadata: _Any = ...
    def __init__(self, value: _Any, **metadata: _Any) -> None: ...

class Delegate(TraitType):
    ctrait_type: _Any = ...
    metadata: _Any = ...
    delegate: _Any = ...
    prefix: _Any = ...
    prefix_type: _Any = ...
    modify: _Any = ...
    def __init__(self, delegate: _Any, prefix: str = ..., modify: bool = ..., listenable: bool = ..., **metadata: _Any) -> None: ...
    def as_ctrait(self): ...

class DelegatesTo(Delegate):
    def __init__(self, delegate: _Any, prefix: str = ..., listenable: bool = ..., **metadata: _Any) -> None: ...

class PrototypedFrom(Delegate):
    def __init__(self, prototype: _Any, prefix: str = ..., listenable: bool = ..., **metadata: _Any) -> None: ...

class Expression(TraitType):
    default_value: str = ...
    info_text: str = ...
    is_mapped: bool = ...
    def validate(self, object: _Any, name: _Any, value: _Any): ...
    def post_setattr(self, object: _Any, name: _Any, value: _Any) -> None: ...
    def mapped_value(self, value: _Any): ...
    def as_ctrait(self): ...

class PythonValue(Any):
    metadata: _Any = ...

class BaseFile(BaseStr):
    info_text: str = ...
    filter: _Any = ...
    auto_set: _Any = ...
    entries: _Any = ...
    exists: _Any = ...
    def __init__(self, value: str = ..., filter: Optional[_Any] = ..., auto_set: bool = ..., entries: int = ..., exists: bool = ..., **metadata: _Any) -> None: ...
    def validate(self, object: _Any, name: _Any, value: _Any): ...
    def create_editor(self): ...

class File(BaseFile):
    def __init__(self, value: str = ..., filter: Optional[_Any] = ..., auto_set: bool = ..., entries: int = ..., exists: bool = ..., **metadata: _Any) -> None: ...

class BaseDirectory(BaseStr):
    info_text: str = ...
    entries: _Any = ...
    auto_set: _Any = ...
    exists: _Any = ...
    def __init__(self, value: str = ..., auto_set: bool = ..., entries: int = ..., exists: bool = ..., **metadata: _Any) -> None: ...
    def validate(self, object: _Any, name: _Any, value: _Any): ...
    def create_editor(self): ...

class Directory(BaseDirectory):
    fast_validate: _Any = ...
    def __init__(self, value: str = ..., auto_set: bool = ..., entries: int = ..., exists: bool = ..., **metadata: _Any) -> None: ...

class BaseRange(TraitType):
    default_value_type: _Any = ...
    default_value: _Any = ...
    def __init__(self, low: Optional[_Any] = ..., high: Optional[_Any] = ..., value: Optional[_Any] = ..., exclude_low: bool = ..., exclude_high: bool = ..., **metadata: _Any) -> None: ...
    def init_fast_validate(self, *args: _Any) -> None: ...
    def validate(self, object: _Any, name: _Any, value: _Any): ...
    def float_validate(self, object: _Any, name: _Any, value: _Any): ...
    def int_validate(self, object: _Any, name: _Any, value: _Any): ...
    def full_info(self, object: _Any, name: _Any, value: _Any): ...
    def create_editor(self): ...

class Range(BaseRange):
    fast_validate: _Any = ...
    def init_fast_validate(self, *args: _Any) -> None: ...

class BaseEnum(TraitType):
    name: _Any = ...
    values: _Any = ...
    def __init__(self, *args: _Any, **metadata: _Any) -> None: ...
    def init_fast_validate(self, *args: _Any) -> None: ...
    def validate(self, object: _Any, name: _Any, value: _Any): ...
    def full_info(self, object: _Any, name: _Any, value: _Any): ...
    def create_editor(self): ...

class Enum(BaseEnum):
    fast_validate: _Any = ...
    def init_fast_validate(self, *args: _Any) -> None: ...

class BaseTuple(TraitType):
    types: _Any = ...
    def __init__(self, *types: _Any, **metadata: _Any) -> None: ...
    no_type_check: _Any = ...
    def init_fast_validate(self, *args: _Any) -> None: ...
    def validate(self, object: _Any, name: _Any, value: _Any): ...
    def full_info(self, object: _Any, name: _Any, value: _Any): ...
    def create_editor(self): ...

class Tuple(BaseTuple):
    fast_validate: _Any = ...
    def init_fast_validate(self, *args: _Any) -> None: ...

class ValidatedTuple(BaseTuple):
    def __init__(self, *types: _Any, **metadata: _Any) -> None: ...
    def validate(self, object: _Any, name: _Any, value: _Any): ...
    def full_info(self, object: _Any, name: _Any, value: _Any): ...

class List(TraitType):
    info_trait: _Any = ...
    default_value_type: _Any = ...
    item_trait: _Any = ...
    minlen: _Any = ...
    maxlen: _Any = ...
    has_items: _Any = ...
    def __init__(self, trait: Optional[_Any] = ..., value: Optional[_Any] = ..., minlen: int = ..., maxlen: _Any = ..., items: bool = ..., **metadata: _Any) -> None: ...
    def validate(self, object: _Any, name: _Any, value: _Any): ...
    def full_info(self, object: _Any, name: _Any, value: _Any): ...
    def create_editor(self): ...
    def inner_traits(self): ...
    def items_event(self): ...

class CList(List):
    def validate(self, object: _Any, name: _Any, value: _Any): ...
    def full_info(self, object: _Any, name: _Any, value: _Any): ...

class Set(TraitType):
    info_trait: _Any = ...
    default_value_type: _Any = ...
    item_trait: _Any = ...
    has_items: _Any = ...
    def __init__(self, trait: Optional[_Any] = ..., value: Optional[_Any] = ..., items: bool = ..., **metadata: _Any) -> None: ...
    def validate(self, object: _Any, name: _Any, value: _Any): ...
    def full_info(self, object: _Any, name: _Any, value: _Any): ...
    def create_editor(self): ...
    def inner_traits(self): ...
    def items_event(self): ...

class CSet(Set):
    def validate(self, object: _Any, name: _Any, value: _Any): ...
    def full_info(self, object: _Any, name: _Any, value: _Any): ...

class Dict(TraitType):
    info_trait: _Any = ...
    default_value_type: _Any = ...
    key_trait: _Any = ...
    value_trait: _Any = ...
    has_items: _Any = ...
    value_handler: _Any = ...
    def __init__(self, key_trait: Optional[_Any] = ..., value_trait: Optional[_Any] = ..., value: Optional[_Any] = ..., items: bool = ..., **metadata: _Any) -> None: ...
    def validate(self, object: _Any, name: _Any, value: _Any): ...
    def full_info(self, object: _Any, name: _Any, value: _Any): ...
    def create_editor(self): ...
    def inner_traits(self): ...
    def items_event(self): ...

AdaptMap: _Any

class BaseClass(TraitType):
    klass: _Any = ...
    def resolve_class(self, object: _Any, name: _Any, value: _Any) -> None: ...
    def validate_class(self, klass: _Any): ...
    def find_class(self, klass: _Any): ...
    def validate_failed(self, object: _Any, name: _Any, value: _Any) -> None: ...

class BaseInstance(BaseClass):
    adapt_default: str = ...
    adapt: _Any = ...
    module: _Any = ...
    klass: _Any = ...
    default_value: _Any = ...
    def __init__(self, klass: Optional[_Any] = ..., factory: Optional[_Any] = ..., args: Optional[_Any] = ..., kw: Optional[_Any] = ..., allow_none: bool = ..., adapt: Optional[_Any] = ..., module: Optional[_Any] = ..., **metadata: _Any) -> None: ...
    def validate(self, object: _Any, name: _Any, value: _Any): ...
    def info(self): ...
    default_value_type: _Any = ...
    def get_default_value(self): ...
    def create_editor(self): ...
    def create_default_value(self, *args: _Any, **kw: _Any): ...
    def allow_none(self) -> None: ...
    def init_fast_validate(self) -> None: ...
    def resolve_class(self, object: _Any, name: _Any, value: _Any) -> None: ...

class Instance(BaseInstance):
    fast_validate: _Any = ...
    def init_fast_validate(self) -> None: ...

class Supports(Instance):
    adapt_default: str = ...
    def post_setattr(self, object: _Any, name: _Any, value: _Any) -> None: ...
    def as_ctrait(self): ...
    def modify_ctrait(self, ctrait: _Any): ...

class AdaptsTo(Supports):
    def modify_ctrait(self, ctrait: _Any): ...

class Type(BaseClass):
    klass: _Any = ...
    module: _Any = ...
    def __init__(self, value: Optional[_Any] = ..., klass: Optional[_Any] = ..., allow_none: bool = ..., **metadata: _Any) -> None: ...
    def validate(self, object: _Any, name: _Any, value: _Any): ...
    def resolve(self, object: _Any, name: _Any, value: _Any): ...
    def info(self): ...
    def get_default_value(self): ...
    def resolve_default_value(self): ...
Subclass = Type

class Event(TraitType):
    trait: _Any = ...
    fast_validate: _Any = ...
    def __init__(self, trait: Optional[_Any] = ..., **metadata: _Any) -> None: ...
    def full_info(self, object: _Any, name: _Any, value: _Any): ...

class Button(Event):
    label: _Any = ...
    values_trait: _Any = ...
    image: _Any = ...
    style: _Any = ...
    orientation: _Any = ...
    width_padding: _Any = ...
    height_padding: _Any = ...
    view: _Any = ...
    def __init__(self, label: str = ..., image: Optional[_Any] = ..., values_trait: Optional[_Any] = ..., style: str = ..., orientation: str = ..., width_padding: int = ..., height_padding: int = ..., view: Optional[_Any] = ..., **metadata: _Any) -> None: ...
    def create_editor(self): ...

class ToolbarButton(Button):
    def __init__(self, label: str = ..., image: Optional[_Any] = ..., style: str = ..., orientation: str = ..., width_padding: int = ..., height_padding: int = ..., **metadata: _Any) -> None: ...

class Either(TraitType):
    trait_maker: _Any = ...
    def __init__(self, *traits: _Any, **metadata: _Any) -> None: ...
    def as_ctrait(self): ...

class Symbol(TraitType):
    info_text: str = ...
    def get(self, object: _Any, name: _Any): ...
    def set(self, object: _Any, name: _Any, value: _Any) -> None: ...

class UUID(TraitType):
    info_text: str = ...
    can_init: _Any = ...
    def __init__(self, can_init: bool = ..., **metadata: _Any) -> None: ...
    def validate(self, object: _Any, name: _Any, value: _Any): ...
    def get_default_value(self): ...

class WeakRef(Instance):
    def __init__(self, klass: str = ..., allow_none: bool = ..., adapt: str = ..., **metadata: _Any) -> None: ...
    def get(self, object: _Any, name: _Any): ...
    def set(self, object: _Any, name: _Any, value: _Any) -> None: ...
    klass: _Any = ...
    def resolve_class(self, object: _Any, name: _Any, value: _Any) -> None: ...

Date: _Any
Datetime: _Any
Time: _Any
AdaptedTo = Supports
BaseUnicode = BaseStr
Unicode = Str
BaseCUnicode = BaseCStr
CUnicode = CStr
BaseLong = BaseInt
Long = Int
BaseCLong = BaseCInt
CLong = CInt
false = Bool
true: _Any
undefined: _Any
ListInt: _Any
ListFloat: _Any
ListStr: _Any
ListUnicode: _Any
ListComplex: _Any
ListBool: _Any
ListFunction: _Any
ListMethod: _Any
ListThis: _Any
DictStrAny: _Any
DictStrStr: _Any
DictStrInt: _Any
DictStrFloat: _Any
DictStrBool: _Any
DictStrList: _Any