import numpy as np
  
class Calculation:
  

    # is there overheating?
    def is_overheating(sensor, threshold=75.0):
        # 75 is the defult temperature that is considered too high
        """
        Checks if the machine is overheating.
        Returns True if temperature exceeds the threshold, else False.
        """
        # show an alert on the dashboard front end if the temperature is high
        return sensor.temperature > threshold

    def calculate_risk(sensor):
        """
        Calculates a risk score for the machine based on sensor data.
        Higher temperature and higher error rate increase risk.
        Returns a float between 0 (low risk) and 1 (high risk).
        """
        temperature = min(max((sensor.temperature - 20) / 80, 0), 1) 
        error = min(max(sensor.error_rate_pct / 100, 0), 1)
        
        # Weighted risk calculation based on the temperature and error rate
        # Does the temperature affects the error rate?
        risk = 0.6 * temperature + 0.4 * error
        # return thr risk level
        if risk < 0.3:
            return "Low"
        elif risk < 0.7:
            return "Medium"
        else:
            return "High"


    def calculate_efficiency(sensor):
        """
        Calculates an efficiency score for the machine.
        Assumes efficiency decreases with high temperature and high error rate.
        Returns a float between 0 (low efficiency) and 1 (high efficiency).
        """
        temperature = min(max((sensor.temperature - 20) / 80, 0), 1)
        error = min(max(sensor.error_rate_pct / 100, 0), 1)
        
        # Efficiency inversely proportional to penalties
        efficiency = max(0, 1 - (0.5 * temperature + 0.5 * error))

        return round(efficiency * 100, 1)    
    
 

    def temperature_error_correlation(sensor_list):
        """
        Simple correlation between temperature and error_rate_pct 
        Returns number between -1 and 1.

        Positive → temperature increases → errors increase

        Negative → temperature increases → errors decrease
        """
        
        temps = [s.temperature for s in sensor_list]
        errors = [s.error_rate_pct for s in sensor_list]
        
        if len(temps) < 2:  # correlation undefined for <2 points
            return 0.0
        
        return round(np.corrcoef(temps, errors)[0, 1], 2)
