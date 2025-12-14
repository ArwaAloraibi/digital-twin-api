from pydantic import BaseModel
from typing import Optional, List
from .sensor_data import SensorDataSchema

class machineSchema(BaseModel):
  machine_id: Optional[int] = True # This makes sure you don't have to explicitly add an id when sending json data
  status: str  
  sensorsData: List[SensorDataSchema] = []

  class Config:
    orm_mode = True
