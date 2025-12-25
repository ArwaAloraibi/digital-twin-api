from pydantic import BaseModel
from typing import Optional, List
from .sensor_data import SensorDataSchema

class machineSchema(BaseModel):
  machine_id: int
  status: str  
  sensor_data: List[SensorDataSchema] = []

  class Config:
    orm_mode = True
