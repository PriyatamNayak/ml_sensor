from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

class DataTransform:
    def __init__(self,data_df):
        self.data=data_df
    def transform(self):
        result_data = pd.pivot_table(self.data, values='tag_val', index=['created_timestamp'],
                                 columns='tag_key').reset_index()
        result_data = result_data.ffill()
        model_data = result_data[result_data['sens_1'].notna()]
        model_data.fillna(0, inplace=True)
        model_data = model_data.set_index('created_timestamp')
        model_data.sort_index(inplace=True)

        X = model_data[['sens_2', 'sens_4', 'sens_5']]
        y = model_data[['sens_1']]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        return  model_data,X_train, X_test, y_train, y_test

