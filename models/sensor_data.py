from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel


class SensorDataModel(BaseModel):
  

    __tablename__ = "sensor_data"  # The name of the table in the database

    machine_id = Column(Integer, ForeignKey("machines.machine_id"), nullable=False)
    temperature = Column(Float)
    power_consumption_kw = Column(Float)
    network_latency_ms = Column(Float)
    error_rate_pct = Column(Float)
    efficiency_status = Column(String)
    
    # ForeignKey establishes a connection to the teas table
    machine = relationship("MachineModel", back_populates="sensor_data")  # Defines the relationship to the MachineModel
