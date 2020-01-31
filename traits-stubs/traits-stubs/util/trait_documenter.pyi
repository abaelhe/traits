from ..has_traits import MetaHasTraits as MetaHasTraits
from ..trait_type import TraitType as TraitType
from sphinx.ext.autodoc import ClassLevelDocumenter
from typing import Any

class TraitDocumenter(ClassLevelDocumenter):
    objtype: str = ...
    directivetype: str = ...
    member_order: int = ...
    priority: int = ...
    @classmethod
    def can_document_member(cls, member: Any, membername: Any, isattr: Any, parent: Any): ...
    def document_members(self, all_members: bool = ...) -> None: ...
    def add_content(self, more_content: Any, no_docstring: bool = ...) -> None: ...
    object_name: Any = ...
    object: Any = ...
    parent: Any = ...
    def import_object(self): ...
    def add_directive_header(self, sig: Any) -> None: ...

def setup(app: Any) -> None: ...
