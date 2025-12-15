from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel


class SensorDataModel(BaseModel):
  

    __tablename__ = "sensor_data"  # The name of the table in the database

    id = Column(Integer, primary_key=True)
    machine_id = Column(Integer, ForeignKey("machines.machine_id"), nullable=False)
    status=Column(String)
    temperature = Column(Float)
    power_consumption_kw = Column(Float)
    network_latency_ms = Column(Float)
    error_rate_pct = Column(Float)
    efficiency_status = Column(String)
    
    # ForeignKey establishes a connection to the teas table
    machine = relationship("MachineModel", back_populates="sensor_data")  # Defines the relationship to the MachineModel
