from datetime import date, datetime
from typing import Union

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from models import *

import logging

from backend_test import fetch_and_convert_by_meal_date, fetch_by_item_id

app = FastAPI()
logger = logging.getLogger(__name__)

VALID_LOCATIONS = {"Hillenbrand", "Earhart", "Wiley", "Ford", "Windsor"}
VALID_MEAL_TYPES = {"Breakfast", "Lunch", "Dinner", "Brunch"}

@app.get("/")
async def read_root() -> Menu:
    try:
        data = await fetch_and_convert_by_meal_date("Hillenbrand", date=date(2025, 9, 21))
        return data
    except Exception as e:
        return {"error": str(e)}

@app.get("/menus/item")
async def get_item(item_id: str = Query(..., description="The ID of the item")) -> ItemOut:
    # Get a specific menu item by its UUID within a location + date menu.
    try:
        data = await fetch_by_item_id(item_id) 
        return data

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/menus")
async def read_menu(
    location: str = Query(..., description="The location of the dining hall"),
    date: str = Query(..., description="The date of the menu in YYYY-MM-DD format")
) -> Menu:
    if location not in VALID_LOCATIONS:
        raise HTTPException(status_code=400, detail=f"Invalid location. Valid locations are: {', '.join(VALID_LOCATIONS)}")
    try:
        format_code = "%Y-%m-%d"
        date_obj = datetime.strptime(date, format_code).date()
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Use YYYY-MM-DD.")
    try:
        data = await fetch_and_convert_by_meal_date(location, date_obj)
        return data
    except Exception as e:
        return {"error": str(e)}

@app.get("/menus/stations")
async def get_menu_stations(
    location: str = Query(..., description="The location of the dining hall"),
    date: str = Query(..., description="The date of the menu in YYYY-MM-DD format"),
    meals: str = Query(..., description="The type of meal (Lunch, Dinner, Brunch, Breakfast, etc)")
) -> StationsOut:
    if location not in VALID_LOCATIONS:
        raise HTTPException(status_code=400, detail=f"Invalid location. Valid locations are: {', '.join(VALID_LOCATIONS)}")
    if meals not in VALID_MEAL_TYPES:
        raise HTTPException(status_code=400, detail=f"Invalid meal type. Valid meal types are: {', '.join(VALID_MEAL_TYPES)}")
    try:
        format_code = "%Y-%m-%d"
        date_obj = datetime.strptime(date, format_code).date()
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Use YYYY-MM-DD.")
    try:
        data = await fetch_and_convert_by_meal_date(location, date_obj)
        mealSlice: list = list(filter(lambda meal: meal["Type"] == meals, data["Meals"]))
        # logging.info(mealSlice)
        if not mealSlice:
            raise HTTPException(status_code=404, detail=f"No meals found for type: {meals}")
        return {
            "Location": location,
            "Date": date,
            "Stations": [stations["Name"] for stations in mealSlice[0]["Stations"]]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))