from datetime import datetime
from http.client import HTTPException
from fastapi import FastAPI, APIRouter
from pydantic import BaseModel, Field
from models.database import db
from playhouse.shortcuts import model_to_dict
from urllib import response
from models.matches import Matches
from peewee import fn
from typing import List, Optional
import peewee
import pydash


router = APIRouter()

class Match(BaseModel):
    id: int
    home_id: int
    away_id: int
    home_goal: int
    away_goal: int
    start_time: str
    place: str

class PatchMatch(BaseModel):
    home_id: Optional[int] = None
    away_id: Optional[int] = None
    home_goal: Optional[int] = None
    away_goal: Optional[int] = None
    start_time: Optional[str] = None
    place: Optional[str] = None

class PostMatch(BaseModel):
    home_id: int
    away_id: int
    home_goal: int
    away_goal: int
    start_time: str
    place: str

@router.post("/admin_api/matches")
async def create_match(match: PostMatch):
    match = Matches.insert(match.__dict__).execute()
    return 204

@router.patch("/admin_api/matches/{match_id}", response_model = Match)
async def edit_match(match_id: str, match: PatchMatch):
    match_dict = match.__dict__

    data = {item: match_dict[item] for item in match_dict if match_dict[item]}
    update = Matches.update(data).where(Mathces.id == match_id).execute()
    result = Matches.select().where(Matches.id == match_id).get()
    return model_to_dict(result)

@router.delete("/admin_api/matches/{match_id}")
async def delete_match(id: str):
    match = Matches.get_by_id(id)
    match.delete_instance()
    return 204