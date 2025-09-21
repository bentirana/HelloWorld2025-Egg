from typing import List, Optional
from pydantic import BaseModel, Field

class Allergen(BaseModel):
    Name: str
    Value: bool


class Item(BaseModel):
    ID: str
    Name: str
    IsVegetarian: bool
    NutritionReady: bool
    Allergens: Optional[List[Allergen]] = None


class Station(BaseModel):
    Name: str
    Items: List[Item]
    IconUrl: Optional[str] = None
    ForegroundColor: Optional[str] = None
    BackgroundColor: Optional[str] = None
    Notes: Optional[str] = None


class Hours_o(BaseModel):
    StartTime: Optional[str] = Field(None, description="Start time of the meal in HH:MM:SS format")
    EndTime: Optional[str] = Field(None, description="End time of the meal in HH:MM:SS format")


class Meal(BaseModel):
    ID: str
    Name: str
    Order: int
    Status: str
    Type: str
    Hours: Optional[Hours_o] = None
    Notes: Optional[str] = None
    Stations: List[Station]


class Menu(BaseModel):
    Location: str
    Date: str
    IsPublished: bool
    Notes: Optional[str] = None
    Meals: List[Meal]


class StationsOut(BaseModel):
    Location: str
    Date: str
    Stations: List[str]


class NutritionFact(BaseModel):
    Name: str
    LabelValue: Optional[str] = None
    Value: Optional[float] = None
    DailyValue: Optional[str] = None
    Ordinal: Optional[int] = None


class NutritionFacts(BaseModel):
    NutritionFact: List[NutritionFact]

class AllergenDetail(BaseModel):
    Name: str
    Value: str


class Allergens(BaseModel):
    Allergen: List[AllergenDetail]


class NutritionDetail(BaseModel):
    Name: str
    LabelValue: Optional[str] = None
    Value: Optional[float] = None
    DailyValue: Optional[str] = None
    Ordinal: int

class ItemOut(BaseModel):
    ID: str
    Name: str
    IsVegetarian: bool
    NutritionReady: bool
    Allergens: List[Allergen]
    Nutrition: List[NutritionDetail]
    Ingredients: str
