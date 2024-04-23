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


@app.route('/', methods=['GET', 'POST'])
def simple_request():
    d = {'message': 'Hej!'}
    return json.dumps(d)

@app.route('/save_signal', methods=['POST'])
def save_signal():
    request_data = request.get_json()
    request_set = set(request_data.keys())
    subset = ds.cols
    if subset.issubset(request_set):
        ds.add_row(request_data["sensor_id"], request_data["timestamp"], request_data["value"])
        return jsonify(message="Signal is received", data=request_data), 200
    else:
        return jsonify(message="Signal is incorrect"), 500

@app.route('/get_sensor/<int:sensor_id>', methods=["GET"])
def get_sensor(sensor_id):
    return jsonify(ds.select_sensor(sensor_id)), 200

@app.route('/get_sensor_ids', methods=['GET'])
def get_ids():
    return jsonify(ds.get_sensor_ids()), 200


if __name__ == "__main__":
    app.run(debug=True)