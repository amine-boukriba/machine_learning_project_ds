from pydantic import BaseModel

class data_input(BaseModel):
    age: int
    bp:float
    sg:float
    al:int
    su:int
    rbc:str
    pc:str
    pcc:str
    ba:str
    bgr:float
    bu:float
    sc:float
    sod:float
    pot:float
    hemo:float
    pcv:float
    wbcc:float
    rbcc:float
    htn:str
    dm:str
    cad:str
    apper:str
    pe:str
    ane:str

