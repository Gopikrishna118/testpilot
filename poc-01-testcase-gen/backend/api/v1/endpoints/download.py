import logging
from pathlib import Path

from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import FileResponse

from core.config import settings

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("")
async def download_excel(path: str = Query(..., description="Relative path to the xlsx file")) -> FileResponse:
    outputs_dir = Path(settings.output_dir).resolve()
    requested   = Path(path).resolve()

    if not requested.is_relative_to(outputs_dir):
        raise HTTPException(status_code=400, detail="Invalid path: must be inside the outputs directory")
    if requested.suffix.lower() != ".xlsx":
        raise HTTPException(status_code=400, detail="Only .xlsx files may be downloaded")
    if not requested.exists():
        raise HTTPException(status_code=404, detail="File not found")

    logger.info("Download | file=%s", requested.name)
    return FileResponse(
        path=str(requested),
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        filename=requested.name,
    )
