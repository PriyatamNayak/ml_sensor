import pandas as pd
import os
from app import cache
from utils.constants import TIMEOUT
from environment.settings import artifact_dir

@cache.memoize(timeout=TIMEOUT)
def query_data():
    # This could be an expensive data querying step
    sensor = pd.read_csv(os.path.join(artifact_dir, "dataset.csv"))
    return sensor.to_json(date_format='iso', orient='split')

def dataframe():    
    return pd.read_json(query_data(), orient='split')