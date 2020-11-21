from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class Heart(BaseModel): 
    cp: int 
    thalach: int
    exang: int
    oldpeak: float
    ca: int