import requests
import allure
from typing import Dict
from tests.config.api_config import APIConfig
from tests.models.pet_models import Pet


class TestPet:
    @allure.title("Добавление нового питомца")
    @allure.description("Тест проверяет создание питомца с валидацией данных ответа")
    @allure.feature("pet")
    def test_add_pet(self, api_config: APIConfig, pet_data: Dict):
        with allure.step("Валидация входных данных"):
            pet_model = Pet(**pet_data)
            
        with allure.step("Отправка запроса на создание питомца"):
            with requests.Session() as session:
                response = session.post(url=api_config.base_url, json=pet_data)

        with allure.step("Проверка статуса и данных ответа"):
            assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
            
            response_data = response.json()
            created_pet = Pet(**response_data)
            
            assert created_pet.id == pet_model.id, "Pet ID mismatch"
            assert created_pet.name == pet_model.name, "Pet name mismatch"
            assert created_pet.status == pet_model.status, "Pet status mismatch" 