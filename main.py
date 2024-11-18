from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from model import SearchData
from schema import SearchDataResponse
import re

app = FastAPI()

pattern = "(22):([\\d]{2}):([\\d]{1,6}):([\\d]+)"


def get_cadastral_number(cadastral_number):
    kns_line = cadastral_number
    kns = (tuple(map((lambda kn: ':'.join(
        list(kn[:-2]) + ['0' * (6 - len(kn[-2])) + kn[-2] if len(kn[-2]) != 6 else kn[-2]] + [str(int(kn[-1]))])),
                     re.findall(pattern, kns_line))),)
    try:
        return kns[0][0]
    except IndexError:
        return ""


@app.get("/costs/{cadastral_cost_id}", response_model=list[SearchDataResponse])
async def get_cost(cadastral_cost_id: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(SearchData).where(SearchData.cadastral_number == get_cadastral_number(cadastral_cost_id)))
    cost = result.scalars().all()
    if cost is None:
        raise HTTPException(status_code=404, detail="Цена не найдена.")
    return cost
