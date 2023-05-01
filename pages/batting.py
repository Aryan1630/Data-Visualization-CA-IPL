import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objs as go
from dash import dash_table
from app import app
from dash import dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from dash import html

#python codes
battingDataset  =  pd.read_csv(r"all_season_batting_card.csv")
batting_columns_to_drop = ['commentary','link','runningOver','runningScore','minutes','name']
battingDataset1 = battingDataset.drop(batting_columns_to_drop, axis=1)


season_dropdown = {
    "label": "Select Season",
    "options": [{"label": season, "value": season} for season in battingDataset["season"].unique()],
    "value": battingDataset["season"].unique()[0],
    "id": "season_dropdown",
}
fig = px.scatter(battingDataset, x="runs", y="strikeRate", color="fullName", hover_name="name", title="Runs vs. Strike Rate")
fig.update_layout(
    xaxis_title="Runs",
    yaxis_title="Strike Rate",
    legend_title="Player Name",
)

fig = px.density_heatmap(battingDataset, x="home_team", y="away_team", z="runs", color_continuous_scale="Viridis")


player_stats = battingDataset.groupby(['season', 'fullName','home_team']).agg({
    'runs': 'sum',
    'fours': 'sum',
    'sixes': 'sum',
    'ballsFaced': 'sum'
})

# Calculate strike rate and add it to the data frame
player_stats['strikeRate'] = (player_stats['runs'] / player_stats['ballsFaced']) * 100

# Reset the index to turn 'fullName' and 'season' into columns
player_stats = player_stats.reset_index()




# Navbar Start
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("OVERALL", href="#", className=" btn navLink orange")),
        dbc.NavItem(dbc.NavLink("BATTING", href="#", className=" btn navLink orange")),
        dbc.NavItem(dbc.NavLink("BOWLING", href="#", className="btn navLink orange")),
        dbc.NavItem(dbc.NavLink("ABOUT US", href="https://www.iplt20.com/about/about-us", className="btn navLink orange", id="offWEb")),
        dbc.NavItem(dbc.NavLink("FAN CONTEST", href="https://www.iplt20.com/fan-contests", className="btn navLink  orange", id="offWEb"))
    ],
    brand="IPL",
    brand_href="#",
    color="transparent",
    className="navbar-color"
)
# Navbar end


#firstContainer Start

firstContainer = html.Div([
    dbc.Container([ 
        html.H1('Batting Stats', className="text-center batHeader"),
        dbc.Row([
            dbc.Col([
                html.P('Total Runs', className="text-center", style={'margin-top':'20px'}),
                html.H3('280713', id="runCount", className="text-center"),

                html.P('Total Fours', className="text-center", style={'margin-top':'20px'}),
                html.H3('25464', id="runCount", className="text-center"),

                html.P('Total Sixes', className="text-center", style={'margin-top':'20px'}),
                html.H3('10643', id="runCount", className="text-center"),
            ], width=2, className="batSidebar"),
            dbc.Col([
                html.Div([
    html.H4("Batsman Runs by Season", className="text-center"),
    dcc.Dropdown(
        id='batsman-dropdown',
        options=[{'label': name, 'value': name} for name in battingDataset['fullName'].unique()],
        value=battingDataset['fullName'].unique()[0]
    ),
    dcc.Graph(id='batsman-graph')
])
            ], width=5),

            dbc.Col([
                html.H4("Fours and Sixes by Season", className="text-center"),
                      html.Div(children=[
           dcc.Graph(id='bar-chart')
])
            ], width=5)
        ])

    ], className="firstContainerContent")
], className="firstContainer")
#firstContainer End


# secondContainer = html.Div([
#     dbc.Container([
#         html.Div(children=[
#            dcc.Graph(id='bar-chart')
# ])
#     ])
# ])


thirdContainer = html.Div([
    dbc.Container([
        html.H1("Runs vs Strike Rate of Every Player in Each season", className="text-center", style={'font-size':'2em'}),
        html.Div([
            dcc.Dropdown(id="season_dropdown", options=season_dropdown["options"], value=season_dropdown["value"]),
    dcc.Graph(id="scatter_plot", figure=fig),
])
    ]),
  dbc.Container([
        html.Div([
    html.H1("Heat Map compairing team score against each other every season", className="text-center"),
    dcc.Graph(id="heatmap", figure=fig),
])
  ], className="heatMapContainer")
], className="secondContainerB")



fourthCountainer = html.Div([
    dbc.Container([

  html.Div([
    html.H1("Top 10 Batsmen in IPL Every Season", style={'font-size':'2em', 'margin-top':'20px','margin-bottom':'20px'}, className='text-center'),
    dcc.Dropdown(
        id='season-dropdown',
        options=[{'label': season, 'value': season} for season in player_stats['season'].unique()],
        value=player_stats['season'].unique()[0]
    ),
    html.Br(),
    html.H3(id='season-header1'),
    dash_table.DataTable(
        id='battable',
        columns=[
            {'name': 'Batsman', 'id': 'fullName'},
            {'name': 'Team', 'id': 'home_team'},
            {'name': 'Season', 'id': 'season'},
            {'name': 'Fours', 'id': 'fours'},
            {'name': 'Sixes', 'id': 'sixes'},
            {'name': 'Runs', 'id': 'runs'},
            {'name': 'Strike Rate', 'id': 'strikeRate'},
        ],
        style_cell={'textAlign': 'left'},
        style_header={
            'backgroundColor': 'rgb(230, 230, 230)',
            'fontWeight': 'bold'
        },
        style_data_conditional=[
            {
                'if': {'row_index': 'odd'},
                'backgroundColor': 'rgb(248, 248, 248)'
            }
        ],
        sort_mode='multi',
        sort_by=[{'column_id': 'runs', 'direction': 'desc'}],
        selected_rows=[],
    )
])

    ])
])

fifthContent = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col([
                html.H5('CONTACT'),
                html.A([
                    html.P('Contact Us')], 
                    href="https://www.iplt20.com/about/contact-us"),
                html.A([
                    html.P('Sponsorship')], 
                    href="https://www.iplt20.com/about/contact-us"),
                html.A([
                    html.P('Privacy Policy')], 
                    href="https://www.iplt20.com/privacy-policy"),
                    ], width=3),
                
            dbc.Col([
                html.H5('NEWS'),
                                html.A([
                    html.P('All News')], 
                    href="https://www.iplt20.com/news"),
                html.A([
                    html.P('Announcements')], 
                    href="https://www.iplt20.com/news/announcements"),
                html.A([
                    html.P('Match Reports')], 
                    href="https://www.iplt20.com/news/match-reports"),
            ], width=3),
            dbc.Col([
                html.H5('GALLERY'),
                html.A([
                    html.P('Photos')], 
                    href="https://www.iplt20.com/photos"),
                html.A([
                    html.P('Mobile Products')], 
                    href="https://www.iplt20.com/mobile-products"),
                html.A([
                    html.P('Highlights')], 
                    href="https://www.iplt20.com/videos/highlights"),
                html.A([
                    html.P('Ipl Moments')], 
                    href="https://www.iplt20.com/videos/ipl-magic"),
            ],width=3),
            dbc.Col([
                html.H5('ABOUT'),
                html.A([
                    html.P('Anti Corruption Policy')], 
                    href="https://www.iplt20.com/about/anti-corruption-policy?id=260"),
                html.A([
                    html.P('Anti Doping Policy')], 
                    href="https://www.iplt20.com/about/anti-doping-policy?id=261"),
                html.A([
                    html.P('TUE application form')], 
                    href="https://www.iplt20.com/about/tue-application-form?id=265"),
                html.A([
                    html.P('News Access Regulations')], 
                    href="https://www.iplt20.com/about/news-access-regulations?id=270"),
            ],width=3)
        ])

    ])
], className="thirdContent container text-center")

footer = dbc.Container([
    html.Hr(),
    dbc.Row([
        dbc.Col([
            html.P([
                "Created by ",
                html.A("AJAY"),
                " with ❤️ using Dash."
            ]),
        ], width={"size": 6, "offset": 3}, className="text-center"),
    ]),
])


#layout design
layout = html.Div([
    firstContainer,
    thirdContainer,
    fourthCountainer,
    fifthContent,
    footer
])


# Define the app callback
@app.callback(
    Output('batsman-graph', 'figure'),
    Input('batsman-dropdown', 'value')
)
def update_batsman_graph(selected_batsman):
    # Filter the batting data by the selected batsman
    batsman_data = battingDataset[battingDataset['fullName'] == selected_batsman]

    # Group the batting data by season and sum the runs for each season
    batting_by_season = batsman_data.groupby('season').agg({'runs': 'sum'}).reset_index()

    # Create the Plotly graph
    fig = px.bar(batting_by_season, x='season', y='runs', title=f'Runs by Season for {selected_batsman}')
    fig.update_xaxes(title='Season')
    fig.update_yaxes(title='Runs')
    return fig


# Define the callbacks
@app.callback(Output("scatter_plot", "figure"), Input("season_dropdown", "value"))
def update_scatter_plot(season):
    filtered_df = battingDataset[battingDataset["season"] == season]
    fig = px.scatter(filtered_df, x="runs", y="strikeRate", color="fullName", hover_name="name")
    fig.update_layout(
        xaxis_title="Runs",
        yaxis_title="Strike Rate",
        legend_title="Player Name",
    )
    return fig



@app.callback(
    Output("heatmap", "figure"),
    Input("season_dropdown", "value"),
)
def update_heatmap(season):
    # Filter the data based on the selected season
    filtered_df = battingDataset[battingDataset["season"] == season]
    
    # Define the new figure
    new_fig = px.density_heatmap(filtered_df, x="home_team", y="away_team", z="runs", color_continuous_scale="Viridis")
    
    return new_fig



@app.callback(Output('bar-chart', 'figure'),
              Input('batsman-dropdown', 'value'))
def update_bar_chart(player):
    # Filter data by selected player
    player_data = battingDataset[battingDataset['fullName']==player]
    # Group data by season and sum fours and sixes
    season_data = player_data.groupby('season', as_index=False)[['fours', 'sixes']].sum()
    # Define colors for each season
    colors = px.colors.qualitative.Pastel
    # Create stacked bar chart
    fig = go.Figure(data=[
        go.Bar(name='Fours', x=season_data['season'], y=season_data['fours'], marker_color=colors),
        go.Bar(name='Sixes', x=season_data['season'], y=season_data['sixes'], marker_color=colors)
    ])
    fig.update_layout(barmode='stack', xaxis_title="Season", yaxis_title="Number of Runs")
    return fig





# Define the callback for updating the table
@app.callback(
    Output('battable', 'data'),
    Output('season-header1', 'children'),
    Input('season-dropdown', 'value')
)
def update_table(season):
    # Filter the data based on the selected season
    filtered_stats = player_stats[player_stats['season'] == season]

    # Sort the data by runs scored and take the top 10 players
    top_10 = filtered_stats.sort_values('runs', ascending=False).head(10)

    # Return the data for the table and the season header
    return top_10.to_dict('records'), f"Season: {season}"

# if __name__ == '__main__':
#     app.run_server(debug=True)
