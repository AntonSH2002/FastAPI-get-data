from pydantic import BaseModel
from datetime import date
from decimal import Decimal


class SearchDataResponse(BaseModel):
    id: int
    cadastral_number: str
    date: date
    normative_act: str
    cadastral_value: Decimal
    note: str
