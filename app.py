# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 11:16:43 2022

@author: User
"""

import models.ml.pipe as pipe
from fastapi import FastAPI
from models.data import data_input
import pandas as pd
from sklearn.preprocessing import StandardScaler
import json
import pickle
app = FastAPI(title="deployment", 
              description="API for machine learning project",
              version="1.0")


@app.on_event('startup')
def load_model():
    file = open('models/ml/model.pkl', 'rb')
    pipe.model= pickle.load(file)
    file.close()
    file = open('models/ml/scaler.pkl', 'rb')
    pipe.scaler=pickle.load(file)
    file.close()
    with open(r'C:\Users\User\Desktop\deploy\utils\dict_mapping.json') as json_file:
     pipe.encoder = json.load(json_file)


@app.get("/")
def home():
    return {"health_check": "OK"}


@app.post('/predict', tags=["predictions"])
async def get_prediction(d_input: data_input):
    #reading data
   raw_data = [d_input.age,d_input.bp,
            d_input.sg,d_input.al,
            d_input.su,d_input.rbc,
            d_input.pc,d_input.pcc,
            d_input.ba,d_input.bgr,
            d_input.bu,d_input.sc,
            d_input.sod,d_input.pot,
            d_input.hemo,d_input.pcv,
            d_input.wbcc,d_input.rbcc,
            d_input.htn,d_input.dm,
            d_input.cad,d_input.apper,
            d_input.pe,d_input.ane]

   data=pd.DataFrame(data=[raw_data],columns=['age', 'bp', 
        'sg', 'al', 'su', 'rbc', 'pc', 'pcc', 'ba', 'bgr', 'bu',
       'sc', 'sod', 'pot', 'hemo', 'pcv', 
       'wbcc', 'rbcc', 'htn', 'dm', 'cad',
       'appet', 'pe', 'ane'])
    #encoding categorical features
   
   for key in pipe.encoder.keys():
       data=data.replace({key: pipe.encoder[key]})
   print(data)
    #scaling data
   data=pipe.scaler.transform(data)
   prediction = pipe.model.predict(data)
   return {"prediction": prediction}
