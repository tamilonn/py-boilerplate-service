from fastapi import APIRouter, Depends, HTTPException
from boilerplate.schemas import ServiceResponse, ErrorResponse, ErrorDetail
from fastapi import status


from boilerplate import schemas
import logging


# initialize logger
logger = logging.getLogger(__file__)
# apiversion to use in service response schema
API_VERSION = '1.0'

router = APIRouter(
    prefix="/boilerplate",
    tags=["boilerplate"],
    responses={404: {"description": "Requested endpoint not available"}},
)

@router.get("/health")
async def health():
    health = {"health":"Service is running successfully!!"}
    service_response= ServiceResponse(success=True, apiversion='',data=health, error=None)
    service_response.apiversion=API_VERSION
    return service_response


@router.get("/error")
async def error():
    errors = [ErrorDetail(reason='failed reason1'), ErrorDetail(reason='failed reason2')]
    error= ErrorResponse(code=403, message='Service failed!!', errors=errors)
    
    service_response= ServiceResponse(success=False, apiversion='', data=None, error=error)
    service_response.apiversion=API_VERSION
    return service_response

