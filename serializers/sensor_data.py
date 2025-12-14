from pydantic import BaseModel

class SensorDataSchema(BaseModel):
    machine_id: int
    temperature: float
    power_consumption_kw: float
    network_latency_ms: float
    error_rate_pct: float
    efficiency_status: str 

    class Config:
        orm_mode = True
