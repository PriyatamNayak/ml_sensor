import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

controls = dbc.Card(
    [
        dbc.FormGroup(
            [
                dbc.Label("Sensor variable"),
                dcc.Dropdown(
                    id="dropdown1",
                    options=[
                        {"label": col, "value": col} for col in ['sensor-1','sensor-2','sensor-4','sensor-5']
                    ],
                    value='sensor-1',
                    className='Sensorselector'
                ),
            ]
        ),


    ],
    body=True,
)

layout = dbc.Container(
    [
        html.H1("Linear Regression Of Sensor data"),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(controls, md=4),
                dbc.Col(dcc.Graph(id='graph1'), md=8),
            ],
            align="center",
        ),


    ],
    fluid=True,
)