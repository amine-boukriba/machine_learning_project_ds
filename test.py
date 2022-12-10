# -*- coding: utf-8 -*-
"""
{
  "age": 48, 
  "bp": 70,
  "sg": 1.005,
  "al": 4,
  "su": 0,
  "rbc": "normal",
  "pc": "abnormal",
  "pcc": "present",
  "ba": "notpresent",
  "bgr": 117,
  "bu": 56,
  "sc": 3.8,
  "sod": 111,
  "pot": 2.5,
  "hemo": 11.2,
  "pcv": 32,
  "wbcc": 6700,
  "rbcc": 3.9,
  "htn": "yes,
  "dm": "no",
  "cad": "no",
  "apper": "poor",
  "pe": "yes",
  "ane": "yes"
}
"""
import pickle
import pandas as pd
import json
file = open('models/ml/model.pkl', 'rb')
model= pickle.load(file)
file.close()


with open(r'C:\Users\User\Desktop\deploy\utils\dict_mapping.json') as json_file:
    encoder = json.load(json_file)
    
    

file = open('models/ml/scaler.pkl', 'rb')
scaler=pickle.load(file)
file.close()


raw_data = [ 48,70, 1.005, 4, 0,"normal","abnormal","present","notpresent", 117,56,3.8,111,2.5,11.2, 32, 6700,3.9,"yes","no","no","poor","yes","yes"]
data=pd.DataFrame(data=[raw_data],columns=['age', 'bp', 
       'sg', 'al', 'su', 'rbc', 'pc', 'pcc', 'ba', 'bgr', 'bu',
      'sc', 'sod', 'pot', 'hemo', 'pcv', 
      'wbcc', 'rbcc', 'htn', 'dm', 'cad',
      'appet', 'pe', 'ane'])

for key in encoder.keys():
    data=data.replace({key: encoder[key]})
data=scaler.transform(data)
prediction = model.predict(data)
print(prediction)