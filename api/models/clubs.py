from models.database import PeeWeeBaseModel
import peewee as p

class Clubs(PeeWeeBaseModel):
    id = p.AutoField()
    name = p.TextField()
    leagues_id = p.IntegerField()
    image = p.TextField()
    stadium = p.TextField()