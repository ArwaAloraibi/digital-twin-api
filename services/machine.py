from typing import List

class Machine:
    def __init__(self, machine_id: int):
        self.machine_id = machine_id

        # Current state (updated every stream tick)
        self.status = None
        self.temperature = None
        self.power_consumption_kw = None
        self.network_latency_ms = None
        self.error_rate_pct = None
        self.efficiency_status = None

        # dictionary to store the data as key → value
        self.history: List[dict] = []


    def update(self, sensor):
     self.status = sensor.status
     self.history.append({
        "temperature": sensor.temperature,
        "power": sensor.power_consumption_kw,
        "latency": sensor.network_latency_ms,
        "error_rate": sensor.error_rate_pct,
        "efficiency": sensor.efficiency_status
    })


    
