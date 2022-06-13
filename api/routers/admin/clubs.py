from http.client import HTTPException
from fastapi import FastAPI, APIRouter
from pydantic import BaseModel, Field
from models.database import db
from playhouse.shortcuts import model_to_dict
from urllib import response
from models.clubs import Clubs
from peewee import fn
from typing import List, Optional
import peewee
import pydash

router = APIRouter()

class Club(BaseModel):
    id: int
    name: str
    leagues_id: int
    image: str
    stadium: str
class PostClub(BaseModel):
    name: str
    leagues_id: int
    image: str
    stadium: str
class PatchClub(BaseModel):
    name: Optional[str] = None
    leagues_id: Optional[str] = None
    image: Optional[str] = None
    stadium: Optional[str] = None

@router.post("/admin_api/clubs")
async def create_club(club: PostClub):
    club = Clubs.insert(club.__dict__).execute()

    return 204


@router.patch("/admin_api/clubs/{club_id}")
async def edit_club(club_id: str, club: PatchClub):
    club_dict = club.__dict__
    data = {item: club_dict[item] for item in club_dict if club_dict[item]}

    update = Clubs.update(data).where(Clubs.id == club_id).execute()
    result = Clubs.select().where(Clubs.id == club_id).get()
    return model_to_dict(result)

@router.delete("/admin_api/clubs/{club_id}")
async def delete_club(club_id: str):
    club = Clubs.get_by_id(club_id)
    club.delete_instance()
    return 204