from pydantic import BaseModel

class SensorDataSchema(BaseModel):
  id: int
  content: str

  class Config:
    orm_mode = True
