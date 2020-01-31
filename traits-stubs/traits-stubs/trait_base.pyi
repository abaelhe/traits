from .constants import ValidateTrait as ValidateTrait
from .etsconfig.api import ETSConfig as ETSConfig
from typing import Any

enumerate = enumerate
SequenceTypes: Any
EnumTypes: Any
ComplexTypes: Any
RangeTypes: Any
TypeTypes: Any
TraitNotifier: str
TraitsCache: str
Uninitialized: Any

class _Uninitialized:
    def __new__(cls): ...
    def __reduce_ex__(self, protocol: Any): ...

Undefined: Any

class _Undefined:
    def __new__(cls): ...
    def __reduce_ex__(self, protocol: Any): ...
    def __eq__(self, other: Any) -> Any: ...
    def __hash__(self) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...

class Missing: ...
class Self: ...

def strx(arg: Any): ...

StringTypes: Any
CoercableTypes: Any

def safe_contains(value: Any, container: Any): ...
def enum_default(values: Any): ...
def class_of(object: Any): ...
def add_article(name: Any): ...
def user_name_for(name: Any): ...
def traits_home(): ...
def verify_path(path: Any): ...
def get_module_name(level: int = ...): ...
def get_resource_path(level: int = ...): ...
def xgetattr(object: Any, xname: Any, default: Any = ...): ...
def xsetattr(object: Any, xname: Any, value: Any) -> None: ...

class HandleWeakRef:
    object: Any = ...
    name: Any = ...
    value: Any = ...
    def __init__(self, object: Any, name: Any, value: Any) -> None: ...

def is_none(value: Any): ...
def not_none(value: Any): ...
def not_false(value: Any): ...
def not_event(value: Any): ...
def is_str(value: Any): ...