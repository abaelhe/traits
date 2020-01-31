from typing import Any, Optional

class ETSToolkitError(RuntimeError):
    toolkit: Any = ...
    message: Any = ...
    args: Any = ...
    def __init__(self, message: str = ..., toolkit: Optional[Any] = ..., *args: Any) -> None: ...

class ETSConfig:
    def __init__(self) -> None: ...
    def get_application_data(self, create: bool = ...): ...
    def get_application_home(self, create: bool = ...): ...
    application_data: Any = ...
    application_home: Any = ...
    company: Any = ...
    toolkit: Any = ...
    def provisional_toolkit(self, toolkit: Any) -> None: ...
    enable_toolkit: Any = ...
    kiva_backend: Any = ...
    user_data: Any = ...