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
        
        self.history: List[dict] = []

        # initialize the machine’s properties.