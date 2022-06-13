from models.database import PeeWeeBaseModel
import peewee as p

class Matches(PeeWeeBaseModel):
    id = p.AutoField()
    home_id = p.IntegerField()
    away_id = p.IntegerField()
    home_goal = p.IntegerField()
    away_goal = p.IntegerField()
    start_time = p.DateTimeField()
    place = p.TextField()

    