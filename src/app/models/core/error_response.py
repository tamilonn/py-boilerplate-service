from .error_detail import ErrorDetail
from dataclasses import dataclass

@dataclass
class ErrorResponse:
    code:int
    message:str
    errors:ErrorDetail

    def __init__(self, code, message, errors):
        self.code=code
        self.message=message
        self.errors=errors