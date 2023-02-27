from fastapi import APIRouter

from apis.user import router as user_router
from apis.task import router as task_router


api_router = APIRouter()
api_router.include_router(user_router, prefix="/user", tags=["users"])
api_router.include_router(task_router, prefix="/task", tags=["tasks"])


@api_router.get('/ping/{value}', status_code=200)
async def ping(value: str):
    return {
        "ping": value
    }
