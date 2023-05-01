import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from dash import html
from dash import dcc
from app import app
from pages import home, batting, bowling, overall


#app = dash.Dash(__name__, use_pages=True)

server = app.server

# Navbar Start
navbar = html.Div([
    dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("HOME", href="/home", className=" btn navLink orange")),
        dbc.NavItem(dbc.NavLink("OVERALL", href="/overall", className=" btn navLink orange")),
        dbc.NavItem(dbc.NavLink("BATTING", href="/batting", className="btn navLink orange")),
        dbc.NavItem(dbc.NavLink("BOWLING", href="/bowling", className="btn navLink orange")),
        dbc.NavItem(dbc.NavLink("ABOUT US", href="https://www.iplt20.com/about/about-us", className="btn navLink orange offWEb")),
        dbc.NavItem(dbc.NavLink("FAN CONTEST", href="https://www.iplt20.com/fan-contests", className="btn navLink  orange offWEb"))
    ],
    brand="IPL",
    brand_href="/home",
    color="transparent",
    className="navbar-color"
)
])


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/bowling':
        return bowling.layout
    elif pathname == '/batting':
        return batting.layout
    elif pathname == '/overall':
        return overall.layout
    else:
        return home.layout



if __name__ == '__main__':
    app.run_server(debug=True)       
