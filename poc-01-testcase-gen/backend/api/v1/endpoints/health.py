from fastapi import APIRouter

from core.config import settings

router = APIRouter()


@router.get("/health")
async def health_check() -> dict:
    return {
        "status": "ok",
        "service": "testcase-gen",
        "model": settings.claude_model,
        "version": "0.1.0",
    }
