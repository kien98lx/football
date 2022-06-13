from http.client import HTTPException
from fastapi import FastAPI, APIRouter
from pydantic import BaseModel, Field
from models.database import db
from playhouse.shortcuts import model_to_dict
from urllib import response
from models.leagues import Leagues
from peewee import fn
from typing import List, Optional
import peewee
import pydash


router = APIRouter()

class League(BaseModel):
    id: int
    name: str
    logo: str
class PostLeague(BaseModel):
    name: str
    logo: str
class PatchLeague(BaseModel):
    name: Optional[str] = None
    logo: Optional[str] = None


@router.get("/admin_api/leagues", tags=["Leagues"], response_model = List[League])
async def get_admin_leagues():
    leagues = Leagues.select().order_by(Leagues.id)
    leagues = [model_to_dict(league) for league in leagues]

    return leagues

@router.post("/admin_api/leagues")
async def create_league(league: PostLeague):
    league = Leagues.insert(league.__dict__).execute()

    return 204
    


@router.patch("/admin_api/leagues/{league_id}",response_model = League)
async def edit_league(league_id: str, league: PatchLeague):
    league_dict = league.__dict__
    # remove none fields
    data = {item: league_dict[item] for item in league_dict if league_dict[item]}

    update = Leagues.update(data).where((Leagues.id == league_id)).execute()
    result = Leagues.select().where(Leagues.id == league_id).get()
    return model_to_dict(result)



@router.delete("/admin_api/leagues/{league_id}")
async def delete_league(id: int):
    league = Leagues.get_by_id(id)
    league.delete_instance()
    return 204