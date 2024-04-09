from tensorflow import keras
import numpy as np

model=keras.models.load_model('C:/Users/Dell/Desktop/programmin/StudentPreformancePredictor/predictionModel/studentPerformance.h5')

def PredictPerformance(a):
    if a[0][2].upper() == 'YES':
        a[0][2]=1

    elif a[0][2].upper() == 'NO':
        a[0][2]=0

    
    pred_val=model.predict(np.array(a))
    return pred_val[0]