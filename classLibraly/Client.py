from peewee import *
from classLibraly.BaseModel import BaseModel


class Client(BaseModel):
    id = PrimaryKeyField(column_name="id")
    first_name = CharField(column_name="first_name",max_length=60)
    second_name = CharField(column_name="second_name", max_length=60)
    third_name = CharField(column_name="third_name", max_length=60,null=True)
    email = CharField(column_name="email",max_length=60)
    phone_number = CharField(column_name="phone_number",max_length=15)
    class Meta:
        table_name = "client"