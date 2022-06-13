from datetime import date, datetime
from difflib import Match
from fastapi import FastAPI, APIRouter

from pydantic import BaseModel
from models.database import db
from playhouse.shortcuts import model_to_dict

from urllib import response
from models.matches import Matches
from peewee import fn
from typing import List

router = APIRouter()

class Match(BaseModel):        #validate thong tin gui len va tra ve
    id: int
    home_id: int
    away_id: int
    home_goal: int
    away_goal: int
    start_time: str
    place: str


@router.get("/user_api/matches", tags=["Matches"], response_model = List[Match])
async def get_matches():
    matches = Matches.select().order_by(Matches.id)
    matches = [model_to_dict(match) for match in matches]

    return matches


@router.get("/user_api/matches/{match_id}", tags=["Matches"], response_model = Match)
async def get_match(match_id: int):
    match = Matches.get_by_id(match_id)
  
    return model_to_dict(match)