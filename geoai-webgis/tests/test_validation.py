import pytest
from backend.modules.air_pollution.common import validate_aoi

def test_missing_aoi():
    with pytest.raises(ValueError):
        validate_aoi({})

def test_polygon_is_accepted():
    aoi={"type":"Polygon","coordinates":[[[112.7,-7.3],[112.8,-7.3],[112.8,-7.2],[112.7,-7.2],[112.7,-7.3]]]}
    assert validate_aoi(aoi)==aoi
