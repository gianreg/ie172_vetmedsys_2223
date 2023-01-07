from datetime import date
from sre_parse import State
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import dash
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output, State
import pandas as pd
from urllib.parse import urlparse, parse_qs

from app import app
from apps import dbconnect as db

layout = html.Div(
    [ 
        html.Div(
            [
            dcc.Store(id='transnew_toload', storage_type='memory', data=0),
            ]
        ),
        html.H2("Transaction Details"),
        html.Hr(),
       dbc.Row(
            [
                dbc.Label("Pet", width=2),
                dbc.Col(
                    html.Div(
                        dcc.Dropdown(
                            id='transnew_pet',
                            clearable=True,
                            searchable=True,
                        ),
                        className="dash-bootstrap"
                    ),
                    width=6,
                ),
            ],
            className="mb-3",
        ),
        dbc.Row(
            [
                dbc.Label("Doctor In Charge", width=2),
                dbc.Col(
                    html.Div(
                        dcc.Dropdown(
                            id='transnew_doctor',
                            clearable=True,
                            searchable=True,
                        ),
                        className="dash-bootstrap"
                    ),
                    width=6,
                ),
            ],
            className="mb-3",
        ),
         dbc.Row(
            [
                dbc.Label("Service Offered", width=2),
                dbc.Col(
                    html.Div(
                        dcc.Dropdown(
                            id='transnew_service',
                            clearable=True,
                            searchable=True,
                        ),
                        className="dash-bootstrap"
                    ),
                    width=6,
                ),
            ],
            className="mb-3",
        ),
        dbc.Row(
            [
                dbc.Label("Amount Paid", width=2),
                dbc.Col(
                    dbc.Input(
                        type="text", id="transnew_paid", placeholder="Enter amount paid"
                    ),
                    width=6,
                ),
            ],
            className="mb-3",
        ),
         dbc.Row(
            [
                dbc.Label("Change Returned", width=2),
                dbc.Col(
                    dbc.Input(
                        type="text", id="transnew_change", placeholder="Enter change returned"
                    ),
                    width=6,
                ),
            ],
            className="mb-3",
         ),
        html.Div(
                dbc.Row(
                [
                    dbc.Label("Wish to delete?", width=2),
                    dbc.Col(
                        dbc.Checklist(
                            id='transnew_removerecord',
                            options=[
                                {
                                'label': "Mark for Deletion",
                                'value': 1
                                }
                            ],
                            style={'fontWeight':'bold'},
                        ),
                        width=6,
                    ),
                ],
                className="mb-3",
            ),
            id = 'transnew_removerecord_div'
        ),
        html.Hr(),
        dbc.Button('Submit', color="secondary", id='transnew_submitbtn', n_clicks=0),
        dbc.Modal(
            [
                dbc.ModalHeader("Saving Progress"),
                dbc.ModalBody("tempmessage", id='transnew_feedback_message'),
                dbc.ModalFooter(
                    dbc.Button(
                        "Okay", id="transnew_closebtn", className="ms-auto", n_clicks=0
                    )
                ),
            ],
            id="transnew_modal",
            is_open=False
        ),
    ],
)


@app.callback(
    [
        Output('transnew_pet','options')
    ],
    [
        Input('url','pathname')
    ]
)
def transpetdropdown(pathname):
    if pathname=='/transactions/trans_new':
        sql = """
        SELECT pet_name as label, pet_id as value
        FROM pets
        WHERE pet_delete_ind = False
        """
        values = []
        cols = ['label', 'value']
        df = db.querydatafromdatabase(sql, values, cols)
     
        pet_options = df.to_dict('records')
        return [pet_options]

    else:
        raise PreventUpdate

    
@app.callback(
    [
        Output('transnew_doctor','options')
    ],
    [
        Input('url','pathname')
    ]
)
def transdoctordropdown(pathname):
    if pathname=='/transactions/trans_new':
        sql = """
        SELECT doctor_name as label, doctor_id as value
        FROM doctors
        WHERE doctor_delete_ind = False
        """
        values = []
        cols = ['label', 'value']
        df = db.querydatafromdatabase(sql, values, cols)
     
        doctor_options = df.to_dict('records')
        return [doctor_options]

    else:
        raise PreventUpdate


@app.callback(
    [
        Output('transnew_service','options')
    ],
    [
        Input('url','pathname')
    ]
)
def transservicedropdown(pathname):
    if pathname=='/transactions/trans_new':
        sql = """
        SELECT service_name as label, service_id as value
        FROM services
        WHERE service_delete_ind = False
        """
        values = []
        cols = ['label', 'value']
        df = db.querydatafromdatabase(sql, values, cols)
     
        service_options = df.to_dict('records')
        return [service_options]

    else:
        raise PreventUpdate