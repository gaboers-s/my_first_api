from fastapi import APIRouter, HTTPException
from app.service import quote_service

router = APIRouter(
    prefix = "/api/quotes",
    tags = ["quotes"]
)   

@router.get("/")
def get_quotes():
    return {"Working"}

@router.get("/all")
def get_quotes():
    return quote_service.get_all_quotes()

@router.get("/random")
def get_quotes():
    quote = quote_service.get_random_quotes()

    if quote is None:
        raise HTTPException(
            status_code= 404,
            details = "No quotes Available"
        )

    return quote