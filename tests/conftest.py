from typing import Dict
import pytest
from tests.config.api_config import APIConfig


@pytest.fixture
def api_config() -> APIConfig:
    return APIConfig()


@pytest.fixture
def pet_data() -> Dict:
    return {
        "id": 10,
        "name": "doggie",
        "category": {
            "id": 1,
            "name": "Dogs"
        },
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    } 