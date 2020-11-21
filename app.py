import uvicorn
from fastapi import FastAPI
from Base import Heart
import numpy as np
import pickle
import pandas as pd
# 2. Create the app object
app = FastAPI()
pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)


@app.post('/predict')
def predict_heart(data:Heart):
    data = data.dict()
    cp=data['cp']
    thalach=data['thalach']
    exang=data['exang']
    oldpeak=data['oldpeak']
    ca = data['ca']
   # print(classifier.predict([[variance,skewness,curtosis,entropy]]))
    prediction = classifier.predict([[cp,thalach,exang,oldpeak,ca]])
    if(prediction[0]>0.5):
        prediction="Yes heart disease"
    else:
        prediction="No it's not a heart disease"
    return {
        'prediction': prediction
    }


if __name__ == '__main__':
    uvicorn.run(app,host='127.0.0.1',port=8000)    