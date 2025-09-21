from datetime import date, datetime
from typing import Union

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from backend_test import fetch_and_convert_by_meal_date, fetch_by_item_id

app = FastAPI()

@app.get("/")
async def read_root() -> dict:
    try:
        data = await fetch_and_convert_by_meal_date("Hillenbrand", date=date(2025, 9, 21))
        return data
    except Exception as e:
        return {"error": str(e)}

@app.get("/menus/item/{item_id}")
async def get_item(item_id: str) -> dict:
    print("this is called")
    # Get a specific menu item by its UUID within a location + date menu.
    try:
        data = await fetch_by_item_id(item_id) 
        return data

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/menus/{location}/{date}")
async def read_menu(location: str, date: str) -> dict:
    format_code = "%Y-%m-%d"
    dateObj = datetime.strptime(date, format_code).date()
    try:
        data = await fetch_and_convert_by_meal_date(location, dateObj)
        return data
    except Exception as e:
        return {"error": str(e)}

@app.get("/menus/{location}/{date}/{meals}/stations")
async def get_menu_stations(location: str, date: str, meals: str) -> dict: 
    # Get all stations for a specific location + date menu.
    format_code = "%Y-%m-%d"
    date_obj = datetime.strptime(date, format_code).date()
    try:
        data = await fetch_and_convert_by_meal_date(location, date_obj)
        mealSlice: list = list(filter(lambda meal: meal["Type"] == meals, data["Meals"]))
        # print([stations["Name"] for stations in mealSlice[0]["Stations"]])
        return {
            "Location": location,
            "Date": date,
            "Stations": [stations["Name"] for stations in mealSlice[0]["Stations"]]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))