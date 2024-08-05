"""
    _summary_

    Returns:
        _type_: _description_
"""

import time
from contextlib import asynccontextmanager
import asyncio

import uvicorn
from fastapi import Depends, FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse

from core.config import settings
from api.api import api_router
from utils.logging import logger


async def run_scheduler():
    while True:
        schedule.run_pending()
        await asyncio.sleep(1)


app = FastAPI(
    title="Min Money",
    root_path="/backend",
)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    """_summary_

    Args:
        request (Request): _description_
        call_next (_type_): _description_

    Returns:
        response: call_next
    """
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

# import routers
app.include_router(api_router)

@app.get("/")
def main(req: Request):
    """_summary_

    Returns:
        _type_: _description_
    """
    root_path = req.scope.get("root_path")
    logger.debug(root_path)

    return RedirectResponse(url=f"{root_path}/docs")

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.API_HOST,
        port=settings.API_PORT,
        workers=settings.API_WORKERS,
        reload=False,
        log_level="info",
        use_colors=True,
        timeout_graceful_shutdown=5,
    )
