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

<strong>Calculation</strong> –> Performs calculations for error rate, efficiency, temperature and power consumed by the machine

<strong>DigitalTwin</strong> –> main class to manage streaming, alerts, and calls the Calculation</br>

### WorkFlow:

1.	Every 2–3 seconds, when the DigitalTwin receives a new row:</br>
2.	Update the engine object (Machine/ Digital Twin)</br>
3.	Insert the new sensor reading into the SQL table (sensor_data)</br>
4.	Calculate error rate, efficiency and trigger alerts</br>
5.	Send results to frontend</br>

### Benefits:

⦁	Maintains full historical data for querying previous states.</br>
⦁	Provides realistic simulation of real-time machine monitoring.</br>


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

### ↳ Efficiency correlation (model vs reality):
this is to analise that the correlation between the tempreature and error with the efficincy is weak and these two attributes doesn't affect the system's efficiency that much


### ERD
![EDR](https://i.imgur.com/ZWApFDj.png)

### Future Enhancements:
- Perform more calculations
- Add Pi charts
- Add new sensors


### FrontEnd Repository:
https://github.com/ArwaAloraibi/digital-twin-frontend-/



