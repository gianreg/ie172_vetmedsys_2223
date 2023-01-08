from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import dash
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

import webbrowser

from app import app
from apps import commonmodules as cm
from apps import home
from apps.pets import pets_home, pets_profile
from apps.owners import owners_home, owners_profile
from apps.transactions import trans_home, trans_new
from apps.services import services_home, services_profile
from apps.doctors import doctor_profile, doctors_home


CONTENT_STYLE = {
    "margin-left": "1em",
    "margin-right": "1em",
    "padding": "1em 1em",
}

app.layout = html.Div(
    [
        dcc.Location(id='url', refresh=True),
        cm.navbar,
        html.Div(id='page-content', style=CONTENT_STYLE),
    ]
)

@app.callback(
    [
        Output('page-content', 'children')
    ],
    [
        Input('url', 'pathname')
    ]
)
def displaypage (pathname):
    ctx = dash.callback_context
    if ctx.triggered:
        eventid = ctx.triggered[0]['prop_id'].split('.')[0]
    else:
        raise PreventUpdate

    if eventid == 'url':
        if pathname in ['/', '/home']:  
                returnlayout = home.layout
        elif pathname == '/transactions':
                returnlayout = trans_home.layout
        elif pathname == '/transactions/trans_new':
                returnlayout = trans_new.layout
        elif pathname == '/pets':
                returnlayout = pets_home.layout
        elif pathname == '/pets/pets_profile':
                returnlayout = pets_profile.layout
        elif pathname == '/owners':  
                returnlayout = owners_home.layout
        elif pathname == '/owners/owners_profile':  
                returnlayout = owners_profile.layout
        elif pathname == '/doctors':  
                returnlayout = doctors_home.layout
        elif pathname == '/doctors/doctor_profile':  
                returnlayout = doctor_profile.layout
        elif pathname == '/services':  
                returnlayout = services_home.layout
        elif pathname == '/services/services_profile':  
                returnlayout = services_profile.layout
        elif pathname == '/inventory':  
                returnlayout = 'inventory_home.layout'
        elif pathname == '/inventory/inventory_profile':  
                returnlayout = 'inventory_profile.layout'
        else:
            raise PreventUpdate
    
    return [returnlayout]

if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:8050/', new=0, autoraise=True)
    app.run_server(debug=False)

    