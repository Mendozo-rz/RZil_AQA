"""Constants for test automation project"""

# API URLs
BASE_URL = "https://swagger.rv-school.ru/api/v3"
PET_ENDPOINT = f"{BASE_URL}/pet"

# Pet Statuses
PET_STATUS_AVAILABLE = "available"
PET_STATUS_PENDING = "pending"
PET_STATUS_SOLD = "sold"

# Default Test Data
DEFAULT_PET = {
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
    "status": PET_STATUS_AVAILABLE
} 