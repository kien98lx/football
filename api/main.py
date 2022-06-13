from fastapi import FastAPI

from routers.user import leagues, clubs, matches
from routers.admin import leagues as admin_leagues
from routers.admin import clubs as admin_clubs
from routers.admin import matches as admin_matches

app = FastAPI()

app.include_router(leagues.router)
app.include_router(clubs.router)
app.include_router(matches.router)

app.include_router(admin_leagues.router)
app.include_router(admin_clubs.router)
app.include_router(admin_matches.router)