import pandas as pd
import json
import requests as r

class Client:

    def get_sensor_ids(self):
        res = r.get('http://127.0.0.1:5000/get_sensor_ids')
        if res.status_code == 200:
            ids = json.loads(res.json())['sensor_ids']
            print("OK")
            return ids
        else:
            print("Error")

    def get_data_from_sensor(self, sensor_id):
        res = r.get('http://127.0.0.1:5000/get_sensor/{}'.format(sensor_id))
        if res.status_code == 200:
            df = pd.DataFrame(json.loads(res.json()))
            print("OK")
            return df
        else:
            print("Error")