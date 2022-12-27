from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import dash
from dash.exceptions import PreventUpdate
from app import app

# CSS Styling for the NavLink components
navlink_style = {
 'color': '#fff'
}

navbar = dbc.Navbar(
 [
        html.A(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                dbc.Col(dbc.NavbarBrand("Vet Med System", className="ml-2")),
                ],
                align="center",
                className="g-0",
            ),
            href="/home",
        ),
        dbc.NavLink("Home", href="/home", style=navlink_style),
        dbc.NavLink("Owners", href="/owners", style=navlink_style),
        dbc.NavLink("Pets", href="/pets", style=navlink_style),
        dbc.NavLink("Doctors", href="/doctors", style=navlink_style),
        dbc.NavLink("Services", href="/services", style=navlink_style),
        dbc.NavLink("Inventory", href="/inventory", style=navlink_style),
    ],
    dark=True,
    color='dark'
    
)