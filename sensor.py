import requests as r
import numpy as np
from datetime import datetime
import random


class Sensor:

    def __init__(self, sensor_id):
        self.id = sensor_id
        x = np.arange(0, 1000)
        self.signal = np.sin(x)

    def get_value(self):
        val = random.choice(self.signal)
        time = datetime.now()
        time = time.strftime("%Y-%m-%d %H:%M:%S")
        return {
            "sensor_id": self.id,
            "timestamp": time,
            "value": val
        }

    def send_data(self):
        response = r.post("http://127.0.0.1:5000/save_signal", json=self.get_value())
        if response.status_code == 200:
            print("Signal is sent successfully!")
        else:
            print(f"Error: {response.status_code}")


if __name__ == "__main__":
    sensor = Sensor()
    sensor.send_data()