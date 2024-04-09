from predictionModel.model import PredictPerformance
from pydantic import BaseModel
from fastapi import FastAPI

class StudentParams(BaseModel):
    hrs:int
    prev_score:int
    extra_act:str
    sleep:int
    sample_qp:int

app=FastAPI()

@app.post('/predict')
async def adding_data_to_model(student_data:StudentParams):
    student_features =[[student_data.hrs,student_data.prev_score,student_data.extra_act,student_data.sleep,student_data.sample_qp]]
    
    pred_output = PredictPerformance(student_features)
    #The item fuction is used to convert the pred_output which was initially a numpy scalar to a Python scalar,
    #this made is possible to be used in the json
    return {'Predicted score':pred_output.item()}