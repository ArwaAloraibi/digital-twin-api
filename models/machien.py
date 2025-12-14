from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship  # Import the relationship function from SQLAlchemy ORM
from .base import BaseModel  # Import the base model for SQLAlchemy
from .sensor_data import SensorDataModel  # Import the SensorDataModel class for establishing relationships

# Inherits from BaseModel, a custom base class that extends SQLAlchemy's Base
class MachineModel(BaseModel):
    __tablename__ = "machines"

    # Specific columns for our machine Table.
    machine_id = Column(Integer, primary_key=True, index=True)
    status = Column(String)

    # Define a relationship with the CommentModel table
    sensor_data = relationship("SensorDataModel", back_populates="machine")
