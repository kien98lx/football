from fastapi import FastAPI, APIRouter

from pydantic import BaseModel
from models.database import db
from playhouse.shortcuts import model_to_dict

from urllib import response
from models.leagues import Leagues
from peewee import fn
from typing import List

router = APIRouter()

class League(BaseModel):        #validate thong tin gui len va tra ve
    id: int
    name: str
    logo: str


@router.get("/user_api/leagues", tags=["Leagues"], response_model = List[League])       #config response model cua list
async def get_leagues():
    leagues = Leagues.select().order_by(Leagues.id)
    leagues = [model_to_dict(league) for league in leagues]
    
    return leagues

@router.get("/user_api/leagues/{league_id}", tags=["Leagues"], response_model = League)
async def get_league(league_id: int):
    league = Leagues.get_by_id(league_id)
  
    return model_to_dict(league)

