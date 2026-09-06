# GeoAI Remote Sensing WebGIS MVP

This is the first functional stage of a portfolio-quality GeoAI Remote Sensing platform, built inside GitHub/Codespaces. It follows the workflow **AOI → Dataset/Module → Date Range → Analysis → Map → Statistics**.

## Implemented now
- Leaflet interactive map
- User-defined polygon and rectangle AOI
- Date range and aggregation controls
- Air Pollution → CO
- Google Earth Engine Sentinel-5P processing
- Mean/min/max statistics over the AOI
- Satellite raster tile overlay
- Validation and human-readable errors
- Secure environment-variable based GEE authentication

## Dataset
- `COPERNICUS/S5P/NRTI/L3_CO`
- Band: `CO_column_number_density`
- Unit: `mol/m²`

This is **column number density**, not a ground-level CO concentration. The MVP intentionally performs no unsupported conversion.

## Run in Codespaces
1. Open this repository in GitHub Codespaces.
2. Open the `geoai-webgis` directory.
3. The dev container installs `requirements.txt` automatically.
4. Create `.env` from `.env.example`.
5. Configure `GEE_PROJECT_ID` and `GOOGLE_APPLICATION_CREDENTIALS`.
6. Start the app:

```bash
cd geoai-webgis
uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload
```

Open forwarded port **8000**.

## GEE setup
Create/use a Google Cloud project with Earth Engine enabled and a service account authorized for Earth Engine. Store the service-account JSON somewhere secure inside the Codespace (not in the repository), then point `GOOGLE_APPLICATION_CREDENTIALS` to it.

If credentials are missing, the API returns an explicit configuration error. It never fabricates results.

## Test
- `GET /api/health` should return `{"status":"ok","service":"geoai-webgis"}`.
- Draw a polygon or rectangle.
- Select dates.
- Click **RUN ANALYSIS**.
- The frontend calls `POST /api/analyze` and displays the returned statistics and GEE raster.

## Not implemented yet
NO2, SO2, time series, advanced charts, CSV/GeoTIFF/PDF export, and the constrained natural-language AI assistant are intentionally deferred until this MVP is verified.
