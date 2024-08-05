from fastapi import Depends, HTTPException, status, APIRouter, Query, Form
from sqlalchemy.orm import Session
from api.deps import get_db

router = APIRouter()

@router.post("/chase_cr_upload", status_code=status.HTTP_200_OK)
async def chase_cr_upload(db: Session = Depends(get_db)):
    return "Hello World"