from pathlib import Path
import os
import ee
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parents[1]
load_dotenv(BASE_DIR / ".env")
GEE_PROJECT_ID = os.getenv("GEE_PROJECT_ID", "").strip()
GEE_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS", "").strip()

def initialize_gee():
    if not GEE_PROJECT_ID:
        raise RuntimeError("GEE_PROJECT_ID is not configured.")
    if not GEE_CREDENTIALS:
        raise RuntimeError("GOOGLE_APPLICATION_CREDENTIALS is not configured.")
    if not Path(GEE_CREDENTIALS).is_file():
        raise RuntimeError("GEE credential file was not found at the configured path.")
    try:
        credentials = ee.ServiceAccountCredentials(None, GEE_CREDENTIALS)
        ee.Initialize(credentials=credentials, project=GEE_PROJECT_ID)
    except Exception as exc:
        raise RuntimeError(f"Google Earth Engine authentication failed: {exc}") from exc
