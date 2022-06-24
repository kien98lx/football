from datetime import date, datetime
from difflib import Match
from sqlite3 import Date
import string
from unittest import result
from fastapi import FastAPI, APIRouter

from pydantic import BaseModel
from models.database import db
from playhouse.shortcuts import model_to_dict

from urllib import response
from models.clubs import Clubs
from models.matches import Matches
from peewee import fn, JOIN
from typing import List

router = APIRouter()

class Match(BaseModel):        #validate thong tin gui len va tra ve
    id: int
    home_id: int
    away_id: int
    home_name: str 
    away_name: str 
    home_logo: str = None
    away_logo: str = None
    home_goal: int = None
    away_goal: int = None
    start_time: date
    place: str
    class Config:
        orm_mode = True

def get_match_info(where_condition=None):
    c1 = Clubs.alias("c1")
    c2 = Clubs.alias("c2")
    # c3 = Clubs.alias("c3")
    # c4 = Clubs.alias("c4")
    query = Matches.select(
        Matches.id, 
        Matches.home_id, 
        Matches.away_id, 
        c1.name.alias("home_name"),
        c2.name.alias("away_name"),
        c1.image.alias("home_logo"),
        c2.image.alias("away_logo"),
        Matches.home_goal,
        Matches.away_goal, 
        Matches.start_time, 
        Matches.place
    ).join(c1, JOIN.LEFT_OUTER, on=(Matches.home_id==c1.id)).join(c2, JOIN.LEFT_OUTER, on=(Matches.away_id==c2.id))
   
    if where_condition:
        query = query.where(where_condition)
    return query


@router.get("/user_api/matches", tags=["Matches"], response_model = List[Match])
async def get_matches(start_time: str):
    
    
    matches = get_match_info()
    if start_time:
        day = int(start_time.split('-')[2])
        month = int(start_time.split('-')[1])
        year = int(start_time.split('-')[0])
        
        matches = matches.where((Matches.start_time.day==day) & (Matches.start_time.month==month) & (Matches.start_time.year==year))
    
    result = list(matches.dicts())


    return result

@router.get("/user_api/matches/{match_id}", tags=["Matches"], response_model = Match)
async def get_match(match_id: int):
    match = get_match_info((Matches.id==match_id))
    
    return match.dicts().get()



