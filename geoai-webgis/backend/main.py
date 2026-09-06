from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from backend.api.routes import router

app = FastAPI(title="GeoAI Remote Sensing WebGIS", version="0.1.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=False, allow_methods=["*"], allow_headers=["*"])
app.include_router(router)
ROOT = Path(__file__).resolve().parents[1]
app.mount("/", StaticFiles(directory=ROOT / "frontend", html=True), name="frontend")
