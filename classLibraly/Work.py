from peewee import *
from classLibraly.BaseModel import BaseModel
from classLibraly.Client import Client
from classLibraly.Jawel import Jawel
from classLibraly.Master import Master

class Work(BaseModel):
    id = PrimaryKeyField(column_name="id")
    work_material = CharField(column_name="work_material",max_length=128)
    defect_description = TextField(column_name="defect_description")
    price = FloatField(column_name="price")
    work_type = CharField(column_name="work_type",max_length=32)
    date_start = DateField(column_name="date_start")
    date_end = DateField(column_name="date_end",null=True)
    work_time = TimeField(column_name="work_time",null=True)
    jawel = ForeignKeyField(Jawel,related_name="work_jawel_id",to_field="id")
    client = ForeignKeyField(Client, related_name="work_client_id", to_field="id")
    master = ForeignKeyField(Master, related_name="work_master_id", to_field="id")
    class Meta:
        table_name="work"
