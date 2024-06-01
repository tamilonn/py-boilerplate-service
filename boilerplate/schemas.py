from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional, TypeVar


"""
    'core model classes'
"""
class ErrorDetail(BaseModel):
    reason:Optional[str]=None


class ErrorResponse(BaseModel):
    code:int
    message:str
    errors:Optional[List[ErrorDetail]]=None


T= TypeVar('T')

class ServiceResponse(BaseModel):
    success: bool
    apiversion: str
    data: T
    error: Optional[ErrorResponse]=None

"""
    'End of core model classes'
"""

class SomeTO(BaseModel):
    config_id: int
    # action: Optional[ActionEnum]=ActionEnum.UNKNOWN
    created_date: Optional[datetime]=None
    updated_date: Optional[datetime]=None

    # If Custom data type (DTO or TO) is used in pydantic model, then add this statement
    class Config:
        arbitrary_types_allowed = True

    def __init__(self, 
                 config_id: int,
                 **kwargs) -> None:
        super(SomeTO, self).__init__(config_id=config_id, **kwargs)








