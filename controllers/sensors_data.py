from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from models.sensor_data import SensorDataModel
from serializers.sensor_data import SensorDataSchema
from services.digital_twin import DigitalTwin
from typing import List
from database import get_db

router = APIRouter()


# Get all sensor data for a specific machine
@router.get("/sensors/{machine_id}", response_model=List[SensorDataSchema])
def get_machine_sensor_data(machine_id: int, db: Session = Depends(get_db)):

    sensor_data = db.query(SensorDataModel).filter(SensorDataModel.machine_id == machine_id).order_by(SensorDataModel.id).all() 
    if not sensor_data:
        raise HTTPException(status_code=404, detail="sensor data not found")
    return sensor_data

# Get the latest sensor data for a specific machine
@router.get("/sensors/{machine_id}/latest", response_model=SensorDataSchema)
def get_latest_sensor_data(machine_id: int, db: Session = Depends(get_db)):
   
    latest_sensor = db.query(SensorDataModel).filter(
        SensorDataModel.machine_id == machine_id
    ).order_by(SensorDataModel.id.desc()).first()

    if not latest_sensor:
        raise HTTPException(status_code=404, detail="No sensor data found for this machine")

    return latest_sensor