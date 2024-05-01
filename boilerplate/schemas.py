from pydantic import BaseModel
from typing import TypeVar, Generic


"""
    'core model classes'
"""
class ErrorDetail():
    reason:str

    def __init__(self, reason):
        self.reason=reason


class ErrorResponse():
    code:int
    message:str
    errors = ErrorDetail

    def __init__(self, code, message, errors):

        self.code=code
        self.message=message
        self.errors=errors


T= TypeVar('T')

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
"""
    'End of core model classes'
"""










