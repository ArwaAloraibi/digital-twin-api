# digital-twin-api

## Backend (digital-twin-api):
<p> A Python-based REST API that simulates a digital twin for an industrial machine. The backend handles user authentication, 
streams filtered sensor data from a manufacturing dataset to simulate real-time operation, stores time-series data in a SQL database, 
calculates machine risk and failure indicators, and generates alerts when operational thresholds are exceeded </p>

### Technologies: 
⦁	Python 3</br>
⦁	SQLAlchemy ORM (Database)</br>
⦁	SQL</br>
⦁	JWT (authentication)</br>
⦁	FastAPI Endpoints</br>
⦁	Uvicorn (API server)</br>

### Classes:
<strong> Machine </strong>–> Represents a single machine, stores sensor data and history.</br>

<strong>Calculation</strong> –> Performs calculations for risk level, failure probability and efficiency (maybe even the engine's current health )</br>

<strong>DigitalTwin</strong> –> main class to manage streaming, alerts, and calls to Calculation</br>

### WorkFlow:

1.	Every 2–3 seconds, when the DigitalTwin receives a new row:</br>
2.	Update the engine object (Engine / DigitalTwin)</br>
3.	Insert the new sensor reading into the SQL table (sensor_data)</br>
4.	Calculate risk / alerts</br>
5.	Send results to frontend</br>

### Benefits:

⦁	Maintains full historical data for querying previous states.</br>
⦁	Provides realistic simulation of real-time machine monitoring.</br>

### entities:

#### User:
id</br>
name</br>
password</br>


#### Machine:
machien_id</br>
status</br>


#### SensorData:
machine_id</br>
temperature             float </br>
power_consumption_kw    float</br>
network_latency_ms      float</br>
error_rate_pct          float</br>
efficiency_status       String           Low/Medium/High</br>

#### The machine is: A network‑connected industrial machine inside a smart factory(CNC Milling Machine)

### Using the temperature we can calculate: 
- Whether the machine is overheating</br>
- How temperature correlates with errors</br>
- Whether high temperature reduces efficiency</br>

### Using the power_conumption_KW we can calculate: 
- How much energy the machine uses under different conditions</br>
- Whether high power usage correlates with low efficiency</br>
- Energy anomalies (sudden jumps or drops)</br>

### Using network_latency_ms, we can measure:
- Whether the machine is experiencing network congestion</br>

### Using error_rate_pct, you can measure:
- How often the machine produces errors</br>
- Whether errors correlate with temperature or latency</br>
- Whether the machine is degrading over time</br>

### ERD
![EDR](https://i.imgur.com/zRsBSwE.png)
