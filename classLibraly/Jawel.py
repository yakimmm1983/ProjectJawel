from peewee import *
from classLibraly.BaseModel import BaseModel

class Jawel(BaseModel):
    id = PrimaryKeyField(column_name="id")
    type = CharField(column_name="type",max_length=16)
    material = CharField(column_name="material",max_length=32)
    class Meta:
        table_name = "jawel"

