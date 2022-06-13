from fastapi import FastAPI, APIRouter

from pydantic import BaseModel
from models.database import db
from playhouse.shortcuts import model_to_dict

from urllib import response
from models.clubs import Clubs
from peewee import fn
from typing import List

router = APIRouter()

class Club(BaseModel):        #validate thong tin gui len va tra ve
    id: int
    name: str
    leagues_id: int
    image: str
    stadium: str

@router.get("/user_api/clubs", tags=["Clubs"], response_model = List[Club])
async def get_clubs():
    clubs = Clubs.select().order_by(Clubs.id)
    clubs = [model_to_dict(club) for club in clubs]

    return clubs


@router.get("/user_api/clubs/{club_id}", tags=["Clubs"], response_model = Club)
async def get_club(club_id: int):
    club = Clubs.get_by_id(club_id)
  
    return model_to_dict(club)
