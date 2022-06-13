from models.database import PeeWeeBaseModel
import peewee as p

class Leagues(PeeWeeBaseModel):
    id = p.AutoField()
    name = p.TextField()
    logo = p.TextField()

    