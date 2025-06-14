import requests
import allure
from tests.config.api_config import APIConfig
from tests.models.pet_models import Pet
from tests.config.constants import DEFAULT_PET


@allure.title("Adding new pet")
@allure.description("Test verifies pet creation with response data validation")
@allure.feature("pet")
def test_add_pet(api_config: APIConfig):
    with allure.step("Prepare test data"):
        pet_model = Pet(**DEFAULT_PET)

    with allure.step("Send POST request to create pet"):
        response = requests.post(url=api_config.base_url, json=DEFAULT_PET)
    
    with allure.step("Verify response status code"):
        assert response.status_code == requests.codes.ok, f"Unexpected status code: {response.status_code}"
    
    with allure.step("Verify created pet data"):
        response_data = response.json()
        created_pet = Pet(**response_data)
        
        assert created_pet.id == pet_model.id, "Pet ID mismatch"
        assert created_pet.name == pet_model.name, "Pet name mismatch"
        assert created_pet.status == pet_model.status, "Pet status mismatch" 