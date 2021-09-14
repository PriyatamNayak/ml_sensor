import pandas as pd
def date_conversion(input_dataframe,date_field):
    input_dataframe[date_field]=pd.to_datetime(input_dataframe[date_field])
    input_dataframe[date_field]=input_dataframe[date_field].apply(lambda x: x.strftime('%Y-%m-%d %H:%M:%S'))
    return input_dataframe