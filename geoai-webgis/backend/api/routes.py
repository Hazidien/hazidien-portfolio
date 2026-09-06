from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Any, Literal
from datetime import date
from backend.modules.air_pollution.co import analyze_co

router = APIRouter(prefix="/api")

class AnalyzeRequest(BaseModel):
    module: Literal["air_pollution"]
    variable: Literal["CO"]
    aoi: dict[str, Any]
    start_date: date
    end_date: date
    aggregation: Literal["mean", "median", "min", "max"] = "mean"

@router.get("/health")
def health():
    return {"status": "ok", "service": "geoai-webgis"}

@router.post("/analyze")
def analyze(request: AnalyzeRequest):
    if request.end_date <= request.start_date:
        raise HTTPException(400, "End date must be after start date.")
    try:
        return analyze_co(request.model_dump())
    except ValueError as exc:
        raise HTTPException(400, str(exc)) from exc
    except RuntimeError as exc:
        raise HTTPException(503, str(exc)) from exc
    except Exception as exc:
        raise HTTPException(500, f"GEE processing failed: {exc}") from exc
