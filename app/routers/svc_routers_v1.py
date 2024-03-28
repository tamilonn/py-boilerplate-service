from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(
    prefix="/persons",
    tags=["persons"],
    responses={404: {"description": "Not found"}},
)

@router.get("/health")
async def health():
    return'Service is running successfully!!'

@router.get("/error")
async def error():
    return'Service failed!!'