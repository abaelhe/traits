from .base_trait_handler import BaseTraitHandler as BaseTraitHandler
from .constants import ComparisonMode as ComparisonMode, DefaultValue as DefaultValue, TraitKind as TraitKind
from .trait_base import Missing as Missing, Self as Self, TraitsCache as TraitsCache, Undefined as Undefined, class_of as class_of
from .trait_dict_object import TraitDictObject as TraitDictObject
from .trait_errors import TraitError as TraitError
from .trait_list_object import TraitListObject as TraitListObject
from .trait_set_object import TraitSetObject as TraitSetObject
from typing import Any, Optional

trait_types: Any

class NoDefaultSpecified: ...

class TraitType(BaseTraitHandler):
    default_value: Any = ...
    metadata: Any = ...
    def __init__(self, default_value: Any = ..., **metadata: Any) -> None: ...
    def init(self) -> None: ...
    default_value_type: Any = ...
    def get_default_value(self): ...
    def clone(self, default_value: Any = ..., **metadata: Any): ...
    def get_value(self, object: Any, name: Any, trait: Optional[Any] = ...): ...
    def set_value(self, object: Any, name: Any, value: Any) -> None: ...
    def __call__(self, *args: Any, **kw: Any): ...
    def as_ctrait(self): ...
    @classmethod
    def instantiate_and_get_ctrait(cls): ...
    def __getattr__(self, name: Any): ...