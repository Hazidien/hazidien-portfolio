from typing import Any

def validate_aoi(aoi: dict[str, Any]):
    if not aoi:
        raise ValueError("AOI is required. Draw a polygon or rectangle on the map.")
    if aoi.get("type") not in {"Polygon", "MultiPolygon"}:
        raise ValueError("AOI must be a Polygon or MultiPolygon.")
    if not aoi.get("coordinates"):
        raise ValueError("AOI geometry is empty.")
    if len(str(aoi["coordinates"])) > 250000:
        raise ValueError("AOI geometry is too large. Please draw a smaller area.")
    return aoi
