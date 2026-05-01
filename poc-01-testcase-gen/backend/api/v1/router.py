from fastapi import APIRouter

from api.v1.endpoints import download, generate, health

router = APIRouter()
router.include_router(health.router, tags=["health"])
router.include_router(generate.router, prefix="/generate", tags=["generate"])
router.include_router(download.router, prefix="/download", tags=["download"])
