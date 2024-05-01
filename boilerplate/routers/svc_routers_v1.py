from fastapi import APIRouter, Depends, HTTPException
from boilerplate.schemas import ServiceResponse, ErrorResponse, ErrorDetail
from boilerplate.database import SessionLocal, get_session
from boilerplate.models import Setup
from datetime import datetime


router = APIRouter(
    prefix="/boilerplate",
    tags=["boilerplate"],
    responses={404: {"description": "Requested endpoint not available"}},
)

@router.get("/health")
async def health():
    health = {"health":"Service is running successfully!!"}
    service_response= ServiceResponse(True, '1.0',health, None)
    return service_response


@router.get("/error")
async def error():
    errors = [ErrorDetail(reason='failed reason1'), ErrorDetail(reason='failed reason2')]
    error= ErrorResponse(403, 'Service failed!!', errors)
    
    # errors.reason='failed'
    service_response= ServiceResponse(False, '1.0', None, error)
    return service_response


@router.get("/create")
async def create():
    
    create = {"I'm in /create endpoint!!"}
    service_response= ServiceResponse(True, '1.0',create, None)
    return service_response
