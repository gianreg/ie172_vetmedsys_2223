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
                                        dbc.Label("Search Transaction Date", width=2),
                                        dbc.Col(
                                            dcc.DatePickerSingle(
                                                id='trans_date_filter',
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
@app.callback(
    [
        Output('transactions_translist', 'children')
    ],
    [
        Input('url', 'pathname'),
        Input('trans_date_filter', 'value'),
    ]
 )
def updateservicelist(pathname, searchterm):
    if pathname == '/transactions':
        sql = """select trans_date, pet_id, doctor_id, service_id, inv_id, inv_qty_used, trans_paid, trans_change
            from transactions
            where not trans_delete_ind
        """
        val = []
        colnames = ['Date', 'Pet', 'Doctor-In-Charge','Service Availed','Inventory Used','Inventory Quantity Used','Amount Paid','Change']
        if searchterm:
            sql += "AND trans_date ILIKE %s"
            val += [f"%{searchterm}%"]
        
        transactions = db.querydatafromdatabase(sql, val, colnames)
        if transactions.shape[0]:
            buttons = []
            for transid in transactions['ID']:
                buttons += [
                    html.Div(
                        dbc.Button('Edit/Delete', href=f"/services/services_profile?mode=edit&id={transid}",
                                    size='sm', color='warning'),
                        style={'text-align': 'center'}
                    )
                ]
            transactions['Edit/Delete Record'] = buttons

            transactions.drop('ID', axis=1, inplace=True)

            table = dbc.Table.from_dataframe(transactions, striped = True, bordered = True, hover = True, size = 'sm')
            return [table]

        else:
            return ["There are no records that match the search term."]
    
    else:
        raise PreventUpdate