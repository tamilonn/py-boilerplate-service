from fastapi import APIRouter, Depends, HTTPException
from app.models.core.response import ServiceResponse
from app.models.core.error_response import ErrorResponse

router = APIRouter(
    prefix="/config",
    tags=["persons"],
    responses={404: {"description": "Requested endpoint not available"}},
)

@router.get("/health")
async def health():
    health = {"health":"Service is running successfully!!"}
    service_response= ServiceResponse(True, '1.0',health, None)
    return service_response


@router.get("/error")
async def error():
    error= ErrorResponse(403, 'Service failed!!', None)
    service_response= ServiceResponse(False, '1.0',None, error)
    return service_response


@router.get("/create")
async def create():
    create = {"I'm in /create endpoint!!"}
    service_response= ServiceResponse(True, '1.0',create, None)
    return service_response
