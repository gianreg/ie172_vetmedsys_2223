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
        elif pathname == '/pets':
                returnlayout = pets_home.layout
        elif pathname == '/pets/pets_profile':
                returnlayout = pets_profile.layout
        elif pathname == '/owners':  
                returnlayout = owners_home.layout
        elif pathname == '/owners/owners_profile':  
                returnlayout = owners_profile.layout
        elif pathname == '/doctors':  
                returnlayout = "This will contain doctor details"
        elif pathname == '/services':  
                returnlayout = "This will contain services details"
        elif pathname == '/inventory':  
                returnlayout = "This will contain inventory details"
        else:
            raise PreventUpdate
    
    return [returnlayout]

if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:8050/', new=0, autoraise=True)
    app.run_server(debug=False)