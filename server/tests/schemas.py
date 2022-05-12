from typing import List

from pydantic import BaseModel


class ScheduleC1Schema(BaseModel):
    meal: float
    car: float
    payment: float


class ScheduleC2ElementSchema(ScheduleC1Schema):
    home: float
    phone: float


class ScheduleC2Schema(BaseModel):
    __root__: List[ScheduleC2ElementSchema]
