import pandas as pd
import pytest

from sensor import Sensor
from client import Client

c = Client()
s1 = Sensor(1)
s2 = Sensor(2)

@pytest.fixture(scope="module", autouse=True)
def setup():
    for _ in range(10):
        s1.send_data()
        s2.send_data()

def test_check_ids():
    ids = c.get_sensor_ids()
    assert 1 in ids and 2 in ids, "Server doesn't have required IDs"

def test_check_dataframe():
    df = c.get_data_from_sensor(1)

    assert isinstance(df, pd.DataFrame)
    assert df.loc[0, "sensor_id"] == 1, "wrong sensor ID"
    assert len(df) == 10
