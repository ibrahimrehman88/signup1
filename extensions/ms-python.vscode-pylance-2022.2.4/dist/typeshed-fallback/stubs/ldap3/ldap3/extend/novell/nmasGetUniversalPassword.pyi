from typing import Any

from ...extend.operation import ExtendedOperation

class NmasGetUniversalPassword(ExtendedOperation):
    request_name: str
    response_name: str
    request_value: Any
    asn1_spec: Any
    response_attribute: str
    def config(self) -> None: ...
    def __init__(self, connection, user, controls: Any | None = ...) -> None: ...
    def populate_result(self) -> None: ...
