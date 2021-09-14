import os
from dash.dependencies import Input, Output
import joblib
import plotly.graph_objs as go
from environment.settings import artifact_dir
import pandas as pd

from app import app
from app import cache
from utils.constants import TIMEOUT


@app.callback(
Output('graph1', 'figure'),
[Input('dropdown1', 'value')]
)
#graph plot and styling
@cache.memoize(timeout=TIMEOUT)
def make_graph(value):
    data=pd.read_csv(os.path.join(artifact_dir, "dataset.csv"))
    if value=="sensor-1":
        # minimal input validation, make sure there's at least one cluster
        model = joblib.load(os.path.join(artifact_dir,"models.pkl"))
        X_test = pd.read_csv(os.path.join(artifact_dir,"X_test.csv"))
        y_test = pd.read_csv(os.path.join(artifact_dir, "y_test.csv"))
        X_test = X_test.set_index('created_timestamp')
        predicted = model.predict(X_test)
        df = y_test
        df['predicted'] = predicted
        plot_data = [
            go.Scatter(
                x=df.created_timestamp,
                y=df['sens_1'],
                name='actual'
            ),
            go.Scatter(
                x=df.created_timestamp,
                y=df['predicted'],
                name='prediction'
            )
        ]

        plot_layout = go.Layout(
            title='Time Series Prediction', xaxis_rangeslider_visible=True
        )
        fig = go.Figure(data=plot_data, layout=plot_layout)

        return fig
    elif value=="sensor-2":
        plot_data = [
            go.Scatter(
                x=data.created_timestamp,
                y=data['sens_2'],
                name='sens_2'
            ),

        ]

        plot_layout = go.Layout(
            title='Sensor-2 values', xaxis_rangeslider_visible=True
        )
        fig = go.Figure(data=plot_data, layout=plot_layout)

        return fig
    elif value == "sensor-4":
        plot_data = [
            go.Scatter(
                x=data.created_timestamp,
                y=data['sens_4'],
                name='sens_4'
            ),

        ]

        plot_layout = go.Layout(
            title='Sensor-4 values', xaxis_rangeslider_visible=True
        )
        fig = go.Figure(data=plot_data, layout=plot_layout)

        return fig

    elif value == "sensor-5":
        plot_data = [
            go.Scatter(
                x=data.created_timestamp,
                y=data['sens_5'],
                name='sens_5'
            ),

        ]

        plot_layout = go.Layout(
            title='Sensor-5 values', xaxis_rangeslider_visible=True
        )
        fig = go.Figure(data=plot_data, layout=plot_layout)

        return fig







