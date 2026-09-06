from pathlib import Path
import json
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
    key_path = Path(GEE_CREDENTIALS)
    if not key_path.is_file():
        raise RuntimeError("GEE credential file was not found at the configured path.")
    try:
        with key_path.open(encoding="utf-8") as handle:
            email = json.load(handle).get("client_email")
        if not email:
            raise ValueError("client_email is missing from the GEE service-account JSON.")
        credentials = ee.ServiceAccountCredentials(email, str(key_path))
        ee.Initialize(credentials=credentials, project=GEE_PROJECT_ID)
    except Exception as exc:
        raise RuntimeError(f"Google Earth Engine authentication failed: {exc}") from exc
