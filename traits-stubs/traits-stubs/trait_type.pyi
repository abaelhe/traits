from .base_trait_handler import BaseTraitHandler as BaseTraitHandler
from .constants import ComparisonMode as ComparisonMode, DefaultValue as DefaultValue, TraitKind as TraitKind
from .trait_base import Missing as Missing, Self as Self, TraitsCache as TraitsCache, Undefined as Undefined, class_of as class_of
from .trait_dict_object import TraitDictObject as TraitDictObject
from .trait_errors import TraitError as TraitError
from .trait_list_object import TraitListObject as TraitListObject
from .trait_set_object import TraitSetObject as TraitSetObject
from typing import Any, Dict, Generic, Optional, Tuple, TypeVar


trait_types: Dict[str, int]


class NoDefaultSpecified:
    ...


_Accepts = TypeVar('_Accepts')

_Stores = TypeVar('_Stores')


class _TraitMixin(Generic[_Accepts, _Stores]):

    def __call__(self, *args, **kwagrs) -> _TraitMixin: ...
    def __get__(self, object: Any, type: Any) -> _Stores: ...
    def __set__(self, object: Any, value: _Accepts) -> None: ...

_Trait = _TraitMixin()


class _TraitType(BaseTraitHandler, Generic[_Accepts, _Stores]):
    default_value: _Stores = ...
    metadata: Dict[str, Any] = ...
    def __init__(self, default_value: _Stores = ..., **metadata: Any) -> None: ...
    def init(self) -> None: ...
    def get_default_value(self) -> Tuple[int, _Stores]: ...
    def clone(self, default_value: _Stores = ..., **metadata: Any) -> 'TraitType': ...
    def get_value(self, object: Any, name: str, trait: Optional[Any] = ...) -> _Stores: ...
    def set_value(self, object: Any, name: str, value: _Accepts) -> None: ...
    def __call__(self, *args: Any, **kw: Any): ...
    def as_ctrait(self): ...
    @classmethod
    def instantiate_and_get_ctrait(cls): ...
    def __getattr__(self, name: Any): ...

    def __get__(self, object: Any, type: Any) -> _Stores: ...
    def __set__(self, object: Any, value: _Accepts) -> None: ...


TraitType = _TraitType[Any, Any]