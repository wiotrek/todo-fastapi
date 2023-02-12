import uvicorn
from fastapi import FastAPI

from apis.base import api_router
from core.config import settings


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
    openapi_url="/api/openapi.json",
    docs_url="/api/docs",
)

app.include_router(api_router, prefix="/api", tags=["api_router"])

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        reload=settings.FASTAPI_RELOAD,
        host=settings.FASTAPI_HOST,
        port=settings.FASTAPI_PORT,
    )
