from flask import Flask, jsonify, request
import json
import pandas as pd

app = Flask(__name__)


class Dataset:
    df = pd.DataFrame(columns=[
        'sensor_id',
        'timestamp',
        'value'
    ])
    cols = set(df.columns)

    def add_row(self, sensor_id, timestamp, value):
        row = [sensor_id, timestamp, value]
        self.df.loc[len(self.df)] = row

    def select_sensor(self, sensor_id):
        data = self.df[self.df["sensor_id"] == sensor_id].reset_index(drop=True)
        return json.dumps({col_name: data[col_name].tolist() for col_name in data.columns})

    def get_sensor_ids(self):
        return json.dumps({"sensor_ids": self.df["sensor_id"].unique().tolist()})

ds = Dataset()


@app.route('/save_signal')  # TODO: add an appropriate method
def save_signal():
    # TODO: use request to get data from sensor and save them in ds;
    # TODO: don't forget to check if there are all required data
    pass


@app.route('/get_sensor')  # TODO: append!!! the endpoint and add an appropriate method
def get_sensor(sensor_id):
    pass  # TODO: send all data from dataset of given sensor_id

@app.route('/get_sensor_ids', methods=['GET'])
def get_ids():
    return jsonify(ds.get_sensor_ids()), 200


if __name__ == "__main__":
    app.run(debug=True)