from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import dash
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output, State
import pandas as pd

from app import app

from apps import dbconnect as db

layout = html.Div(
    [
        html.H2("Transactions"),
        html.Hr(),
        dbc.Card(
            [
                dbc.CardHeader(html.H4("Transaction List")),
                dbc.CardBody(
                    [
                        dbc.Button("New Transaction", color="secondary", href = '/transactions/trans_new?mode=add'),
                        html.Hr(),
                        html.Div(
                            [
                                html.H6("Find Transaction",style={'fontweight':'bold'}),
                                html.Hr(),
                                dbc.Row(
                                    [
                                        dbc.Label("Search Transaction ID", width=2),
                                        dbc.Col(
                                            dbc.Input(
                                                type='text',
                                                id='trans_id_filter',
                                                placeholder='Enter Transaction ID'
                                            ),
                                            width=6,
                                        ),
                                    ],
                                className='mb-3',
                                ),
                                html.Div(
                                    "This will contain the table for transactions",
                                    id="transactions_translist"
                                )
                            ]
                        )
                    ]
                )
            ]
        )
    ]
)