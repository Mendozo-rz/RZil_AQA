from dataclasses import dataclass


@dataclass
class APIConfig:
    base_url: str = "https://swagger.rv-school.ru/api/v3/pet" 