from fastapi import FastAPI
# from controllers.machines import router as MachinesRouter
# from controllers.sensors_data import router as Sensors_dataRouter
from controllers.users import router as UserRouter
from models.base import Base
from models.machine import MachineModel
from models.sensor_data import SensorDataModel
from database import engine
Base.metadata.create_all(bind=engine)

app = FastAPI()

# app.include_router(MachinesRouter, prefix="/api")
# app.include_router(Sensors_dataRouter, prefix="/api")
app.include_router(UserRouter, prefix="/api")

@app.get('/')
def home():
    return 'Hello World!'

