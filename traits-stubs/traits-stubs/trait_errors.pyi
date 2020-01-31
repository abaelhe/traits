from .trait_base import class_of as class_of
from typing import Any, Optional

def repr_type(obj: Any): ...

class TraitError(Exception):
    args: Any = ...
    name: Any = ...
    info: Any = ...
    value: Any = ...
    desc: Any = ...
    prefix: str = ...
    def __init__(self, args: Optional[Any] = ..., name: Optional[Any] = ..., info: Optional[Any] = ..., value: Optional[Any] = ...) -> None: ...
    object: Any = ...
    def set_desc(self, desc: Any, object: Optional[Any] = ...) -> None: ...
    def set_prefix(self, prefix: Any) -> None: ...
    def set_args(self) -> None: ...

class TraitNotificationError(Exception): ...

class DelegationError(TraitError):
    args: Any = ...
    def __init__(self, args: Any) -> None: ...