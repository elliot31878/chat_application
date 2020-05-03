from peewee import ( 
    CharField
)
from .base_model import BaseModel
class User(BaseModel):
    username = CharField(unique=True,max_length=20)
    password = CharField(max_length=20)