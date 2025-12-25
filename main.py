from fastapi import FastAPI
from controllers.machines import router as MachinesRouter
from controllers.sensors_data import router as Sensors_dataRouter
from controllers.users import router as UserRouter
from models.base import Base
from database import engine
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://127.0.0.1:5173",
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(MachinesRouter, prefix="/api")
app.include_router(Sensors_dataRouter, prefix="/api")
app.include_router(UserRouter, prefix="/api")

@app.get('/')
def home():
    return 'Hello World!'

