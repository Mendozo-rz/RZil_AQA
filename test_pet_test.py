import requests
import allure

base_url = "https://swagger.rv-school.ru/api/v3/pet"


class TestPet:

    @allure.title("Добавление нового питомца")
    @allure.description("Тест проверяет, что можно добавить питомца с корректными данными и получить статус 200")
    @allure.feature("pet")
    def test_add_pet(self):
        with allure.step("Подготовка данных"):
            data = {
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

        with allure.step("Отправка запроса на создание питомца"):
            response = requests.post(url=base_url, json=data)

        with allure.step("Проверка статуса"):
            assert response.status_code == 200
