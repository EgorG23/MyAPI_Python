from typing import Literal
from pydantic import BaseModel, PositiveInt, PositiveFloat, NonNegativeInt, NonNegativeFloat, Field


class ApartmentRequest(BaseModel):
    housing_type: Literal["Новостройка", "Вторичка"]
    district: Literal["Московский", "Нижегородский", "Канавинский", "Сормовский",
    "Автозаводский", "Ленинский", "Кстовский", "Советский",
    "Приокский", "Горьковская"]
    rooms: PositiveInt
    is_studio: Literal["Да", "Нет"]
    total_area: PositiveFloat
    living_area: PositiveFloat
    kitchen_area: NonNegativeFloat
    floor: NonNegativeInt
    num_floors: PositiveInt
    bathrooms_type: Literal["Совмещенный, Раздельный", "Раздельный", "Совмещенный"]
    num_loggia: NonNegativeInt
    num_balcony: NonNegativeInt
    kitchen_and_living: Literal["Да", "Нет"]
    condition: Literal["Без отделки", "Предчистовая", "Чистовая", "Косметический", "Евро",
    "Требует ремонта", "Дизайнерский"]
    ceiling_height: PositiveFloat
    nearest_metro_st: Literal['Горьковская', "Парк культуры", "Чкаловская", "Ленинская",
    "Буревестник", "Стрелка", "Пролетарская", "Московская", "Заречная", "Комсомольская"]
    minutes_to_metro: PositiveFloat
    num_freight_lift: NonNegativeInt
    num_passenger_lift: NonNegativeInt
    parking_type: Literal["Открытая", "Подземная", "Подземная, открытая"]
    building_type: Literal["Кирпичный", "Монолитно-кирпичный", "Монолитный", "Панельный", "Блочный"]
    furniture: Literal["Да", "Нет"]
    deal_type: Literal["Долевое участие (214-ФЗ)", "Свободная продажа", "Альтернативная"]
    house_completion_year: PositiveInt = Field(gt=1700, lt=2041)
    first_floor_is_com: Literal["Да", "Нет"]
    playground: Literal["Да", "Нет"]
    floor_ratio: PositiveFloat = 1
    living_ratio: PositiveFloat = 1
