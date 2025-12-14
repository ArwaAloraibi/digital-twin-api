from fastapi import FastAPI
from controllers.machines import router as MachinesRouter
from controllers.sensors_data import router as Sensors_dataRouter
from controllers.users import router as UserRouter

app = FastAPI()

app.include_router(MachinesRouter, prefix="/api")
app.include_router(Sensors_dataRouter, prefix="/api")
app.include_router(UserRouter, prefix="/api")

@app.get('/')
def home():
    return 'Hello World!'

