"""
  _summary_
"""

from fastapi import APIRouter

from api.endpoints import chase_cr_upload

api_router = APIRouter()
api_router.include_router(chase_cr_upload.router, tags=["Upload"])
