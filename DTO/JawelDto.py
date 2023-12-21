from classLibraly.Jawel import Jawel

def InsertJawel(type,material):
    jawel = Jawel(type = type,material = material)
    jawel.save()
    return jawel