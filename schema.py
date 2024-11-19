from pydantic import BaseModel
from datetime import date


class SearchDataResponse(BaseModel):
    id: int
    cadastral_number: str
    date: date
    normative_act: str
    cadastral_value: float
    note: str
