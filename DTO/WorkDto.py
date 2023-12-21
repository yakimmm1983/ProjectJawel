from classLibraly.Jawel import Jawel
from classLibraly.Client import Client
from classLibraly.Master import Master
from classLibraly.Work import Work
import datetime

def InsertWork(client,master,price,defect_description,work_type,jawel):
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    work = Work(date_start = date,client = client,master = master,
                price = price,
                defect_description = defect_description,
                work_type = work_type,
                jawel = jawel)
    work.save()
    return work
def EndWork (work:Work,time):
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    work.date_end = date
    work.work_time = time
    work.save()
    return work