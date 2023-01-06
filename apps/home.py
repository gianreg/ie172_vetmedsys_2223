from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import dash
from dash.exceptions import PreventUpdate
import pandas as pd

layout = html.Div(
    [
        html.H2('Welcome to the Vet Med Database System!'),
        html.Hr(),
        html.Div(
            [
                html.Span("Thru this app, you can manage a vet med database."),
                html.Br(),
                html.Span("This page will contain the dashboard"),
                html.Br(),
                html.Br(),
                html.Span("Contact support if you need assistance!",
                style={'font-style':'italic'}),
            ]
        )
    ]
)