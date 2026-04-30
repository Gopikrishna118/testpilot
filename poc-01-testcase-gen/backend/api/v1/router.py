from fastapi import APIRouter

from api.v1.endpoints import generate, health

router = APIRouter()
router.include_router(health.router, tags=["health"])
router.include_router(generate.router, prefix="/generate", tags=["generate"])
