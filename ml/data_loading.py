import pandas as pd
import numpy as np
from os.path import join, dirname
from utils.date_conversion_dataframe import date_conversion
from functools import reduce


data_dir= join(dirname(__file__),"input_feed")



class DataLoading:
    def __init__(self):
        self.sensor1_file = join(data_dir,"sensor_1.xlsx")
        self.sensor2_file = join(data_dir,"sensor_2.csv")
        self.sensor4_file = join(data_dir, "sensor_4.parquet")
        self.sensor4_diff_file = join(data_dir, "sensor_4_diff_date.pickle")
        self.sensor5_file = join(data_dir, "sensor_5.json")

    @staticmethod
    def read_files(file_location,file_type):
        if file_type.lower()== "xls":
            return pd.read_excel(file_location)
        elif file_type.lower()== "csv":
            return pd.read_csv(file_location)
        elif file_type.lower()== "json":
            return pd.read_json(file_location).transpose()
        elif file_type.lower()== "pickle":
            return pd.read_pickle(file_location)
        elif file_type.lower() == "parquet":
            return pd.read_parquet(file_location,engine="fastparquet")

    def load_data(self):
        df_sensor1 = self.read_files( self.sensor1_file ,"xls")
        df_sensor2 = self.read_files(self.sensor2_file, "csv")
        df_sensor4 = self.read_files(self.sensor4_file, "parquet")
        df_sensor4_dif = self.read_files(self.sensor4_diff_file, "pickle")
        df_sensor5 = self.read_files(self.sensor5_file, "json")
        df_sensor1 = date_conversion(df_sensor1, 'created_timestamp')
        df_sensor2 = date_conversion(df_sensor2, 'created_timestamp')
        df_sensor4 = date_conversion(df_sensor4, 'created_timestamp')
        df_sensor4_dif = date_conversion(df_sensor4_dif, 'created_timestamp')
        df_sensor5 = date_conversion(df_sensor5, 'created_timestamp')

        data_frames = [df_sensor1.fillna(np.nan), df_sensor2.fillna(np.nan), df_sensor4.fillna(np.nan),
                       df_sensor4_dif.fillna(np.nan), df_sensor5.fillna(np.nan)]

        df_merged = reduce(lambda left, right: pd.merge(left, right, how="outer"), data_frames)
        df_merged['tag_val'] = np.where(df_merged['tag_quality'] == "Bad", np.nan, df_merged['tag_val'])
        return df_merged





