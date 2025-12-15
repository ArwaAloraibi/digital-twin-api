import time
from typing import List
from data.machine_data import sensor_data_list, machines_list
from services.machine import Machine
from services.calculation import Calculation
from database import get_db
from models.sensor_data import SensorDataModel
from sqlalchemy.orm import Session

# controls how data flows, when it flows, and what happens to it.

class DigitalTwin:
    def __init__(self, machine_id: int, db: Session):
        self.db = db #to insert sensor data into SQL
        self.machine = Machine(machine_id)

        # filter sensor data for this machine
        self.sensor_data_stream = [sensor for sensor in sensor_data_list if sensor.machine_id == machine_id]
        
        
    # Simulates real-time sensor streaming
    def start_stream(self, interval_sec: float = 2.0):
        for sensor in self.sensor_data_stream:
            
            # 1. Update machine object (triggres the update def in the machine class)
            self.machine.update(sensor)

            # 2. Insert sensor data into DB
            self._insert_sensor_data(sensor)

            # 3. Calculation
            risk = Calculation.calculate_risk(sensor)
            efficiency = Calculation.calculate_efficiency(sensor)

            # 4. Print or return results (later, send to frontend)
            print(f"[Machine {self.machine.machine_id}] Risk: {risk}, Efficiency: {efficiency}")

            # Wait for next data point
            time.sleep(interval_sec)

    def _insert_sensor_data(self, sensor):
        db_sensor = SensorDataModel(
            machine_id=sensor.machine_id,
            temperature=sensor.temperature,
            power_consumption_kw=sensor.power_consumption_kw,
            network_latency_ms=sensor.network_latency_ms,
            error_rate_pct=sensor.error_rate_pct,
            efficiency_status=sensor.efficiency_status
        )
        self.db.add(db_sensor)
        self.db.commit()