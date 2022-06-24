from fastapi import FastAPI, APIRouter

from pydantic import BaseModel
from models.database import db
from playhouse.shortcuts import model_to_dict

from urllib import response
from models.clubs import Clubs
from models.matches import Matches
from peewee import fn
from typing import List

router = APIRouter()

class Club(BaseModel):        #validate thong tin gui len va tra ve
    id: int
    name: str
    leagues_id: int
    image: str = None
    stadium: str
    points: int = None

def get_club_points(club_id: int):
    matches = Matches.select().where((Matches.home_id==club_id) | (Matches.away_id==club_id))
    points = 0
    matches = (model_to_dict(match) for match in matches)
    for match in matches:
  
        if match['home_goal'] == match['away_goal']:
            points += 1
        elif (match['home_goal'] > match['away_goal']) and (match['home_id'] == club_id):
            points += 3
        elif (match['home_goal'] < match['away_goal']) and (match['away_id'] == club_id):
            points += 3
    
    return points



@router.get("/user_api/clubs", tags=["Clubs"], response_model = List[Club])
async def get_clubs(league_id: str):
    clubs = Clubs.select().where(Clubs.leagues_id==league_id).order_by(Clubs.id)
    
    clubs = [model_to_dict(club) for club in clubs]
   
    for club in clubs:
        club_point = get_club_points(club['id'])
        club['points'] = club_point
    
    return clubs


@router.get("/user_api/clubs/{club_id}", tags=["Clubs"], response_model = Club)
async def get_club(club_id: int):
    club = Clubs.get_by_id(club_id)
  
    return model_to_dict(club)
