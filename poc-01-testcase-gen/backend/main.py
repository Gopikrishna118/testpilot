from contextlib import asynccontextmanager
import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from api.v1.router import router as v1_router
from core.config import settings

logging.basicConfig(level=settings.log_level, format="%(asctime)s %(levelname)s %(name)s — %(message)s")


@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.getLogger(__name__).info("testcase-gen starting | model=%s", settings.claude_model)
    yield
    logging.getLogger(__name__).info("testcase-gen shutting down")


app = FastAPI(
    title="TestPilot — PoC 01: Test Case Generator",
    version="0.1.0",
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url=None,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
    allow_credentials=False,
)

app.include_router(v1_router, prefix="/api/v1")

app.mount("/", StaticFiles(directory="static", html=True), name="static")
