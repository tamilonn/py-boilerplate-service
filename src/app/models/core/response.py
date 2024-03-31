from typing import TypeVar, Generic
from dataclasses import dataclass
from app.models.core.error_response import ErrorResponse

T= TypeVar('T')

@dataclass
class ServiceResponse(Generic[T]):
    success: bool
    apiversion: str
    data: T
    error: ErrorResponse

    def __init__(self, success, apiver, T, err):
        self.success= success
        self.apiversion= apiver
        self.data= T
        self.error= err