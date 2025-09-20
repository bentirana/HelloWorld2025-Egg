from datetime import date, datetime
from typing import Union

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from backend_test import fetch_and_convert

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
async def read_root() -> dict:
  
    try:
        data = await fetch_and_convert("Hillenbrand", date=date(2025, 9, 21))
        return data
    except Exception as e:
        return {"error": str(e)}

@app.get("/menus/{location}/{date}")
async def read_menu(location: str, date: str) -> dict:
    format_code = "%Y-%m-%d"
    dateObj = datetime.strptime(date, format_code).date()
    try:
        data = await fetch_and_convert(location, dateObj)
        return data
    except Exception as e:
        return {"error": str(e)}



@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}