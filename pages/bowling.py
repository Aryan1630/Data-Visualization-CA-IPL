import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
import plotly.graph_objs as go
from dash import dash_table
import dash
from dash import dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from dash import html
from app import app
from dash.exceptions import PreventUpdate


#python codes
bowlingDataset  =  pd.read_csv(r"D:\DV\IPL 2008-2022\all_season_bowling_card.csv")



oversTotal = int(bowlingDataset['overs'].sum())
wicketsTaken = bowlingDataset['wickets'].sum()
maidensBowled =  bowlingDataset['maidens'].sum()
total_bowlers = len(bowlingDataset["fullName"].unique())


player_stats = bowlingDataset.groupby(['season', 'fullName','home_team']).agg({
    'overs': 'sum',
    'wickets': 'sum',
    'dots': 'sum',
    'wides': 'sum',
    'noballs': 'sum'
})

# Reset the index to turn 'fullName' and 'season' into columns
player_stats = player_stats.reset_index()


bowlingDataset['economyRate'] = bowlingDataset['economyRate'].replace('-', 0)
bowlingDataset['economyRate'] = bowlingDataset['economyRate'].astype(float)

df_grouped = bowlingDataset.groupby(["season", "fullName"]).mean(numeric_only=True).reset_index()


bowlingDataset["total_runs_conceded"] = bowlingDataset["wides"] + bowlingDataset["noballs"] + bowlingDataset["conceded"]


#app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, 'assets/style.css', "https://fonts.googleapis.com/css2?family=Yeseva+One&family=Bruno+Ace+SC&display=swap"], external_scripts=['assets/main.js'])



firstCOntainer = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col([
                    html.Div([
                        html.P("Total Number of Bowlers", className="text-center"),
                        html.H2(f'{total_bowlers}', className='text-center'),
                        html.P("Number of Overs Bowled", className="text-center"),
                        html.H2(f'{oversTotal}', className='text-center'),
                        html.P("Number of Wickets Taken", className="text-center"),
                        html.H2(f'{wicketsTaken}', className='text-center'),
                        html.P("Number of Maidens Bowled", className="text-center"),
                        html.H2(f'{maidensBowled}', className='text-center'),
                    ])
            ], width=2, className="bowlsidebar"),


            dbc.Col([


                html.H1("Top 10 Batsmen in IPL Every Season", style={'font-size':'2em', 'margin-top':'20px','margin-bottom':'20px'}, className='text-center'),
    dcc.Dropdown(
        id='season-dropdown',
        options=[{'label': season, 'value': season} for season in player_stats['season'].unique()],
        value=player_stats['season'].unique()[0]
    ),
    html.Br(),
    html.H3(id='season-header'),
    dash_table.DataTable(
        id='table',
        columns=[
            {'name': 'Bowler', 'id': 'fullName'},
            {'name': 'Team', 'id': 'home_team'},
            {'name': 'Season', 'id': 'season'},
            {'name': 'Wickets', 'id': 'wickets'},
            {'name': 'Dot Ball', 'id': 'dots'},
            {'name': 'Wides', 'id': 'wides'},
            {'name': 'No Balls', 'id': 'noballs'},
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
        sort_by=[{'column_id': 'wickets', 'direction': 'desc'}],
        selected_rows=[],
    )              
            ])
        ])
    ])
], className="bowlerFirstContainer")



secondContainer = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col([
                html.H4('Bowlers Economy Rate based on the season they played', className="text-center"),
                html.Div([
                   dcc.Dropdown(
                    id="bowler-dropdown",
                    options=[{"label": name, "value": name} for name in df_grouped["fullName"].unique()],
                    value=df_grouped["fullName"].iloc[0],
                ),
            dcc.Graph(id="bowler-economy-line-chart"),
            ])
            ]),
            dbc.Col([
                html.H4('Runs conceded', className="text-center"),
                    html.Div([
    dcc.Dropdown(
        id="match-dropdown",
        options=[{"label": name, "value": name} for name in bowlingDataset["match_name"].unique()],
        value=bowlingDataset["match_name"].iloc[0],
    ),
    dcc.Graph(id="team-runs-bar-chart"),
])

            ])
        ])
    ])
],className="secondContainer")


thirdContainer = html.Div([
    dbc.Container([
  html.Div([
    dcc.Dropdown(
        id="bowler-dropdown1",
        options=[{"label": name, "value": name} for name in bowlingDataset["fullName"].unique()],
        value=bowlingDataset["fullName"].iloc[0],
    ),
    dcc.Graph(id="bowler-heatmap"),
])
    ])
], className="BthirdContainer")




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



layout = html.Div([
    firstCOntainer,
    secondContainer,
    thirdContainer,
    fifthContent,
    footer
])

# @app.callback(
#     Output('graph', 'figure'),
#     [Input('season-dropdown', 'value'),
#      Input('player-dropdown', 'value')])
# def update_figure(selected_season, selected_player):
#     filtered_df = bowlingDataset[(bowlingDataset['season'] == selected_season) & (bowlingDataset['fullName'] == selected_player)]
#     fig = px.line(filtered_df, x='match_name', y='economyRate', title='Economy Rate Graph')
#     return fig



# Define the callback for updating the table
@app.callback(
    Output('table', 'data'),
    Output('season-header', 'children'),
    Input('season-dropdown', 'value')
)
def update_table(season):
    # Filter the data based on the selected season
    filtered_stats = player_stats[player_stats['season'] == season]

    # Sort the data by runs scored and take the top 10 players
    top_10 = filtered_stats.sort_values('wickets', ascending=False).head(10)

    # Return the data for the table and the season header
    return top_10.to_dict('records'), f"Season: {season}"



@app.callback(
    dash.dependencies.Output("bowler-economy-line-chart", "figure"),
    [dash.dependencies.Input("bowler-dropdown", "value")])
def update_line_chart(selected_bowler):
    # Filter data for selected bowler
    df_bowler = df_grouped[df_grouped["fullName"] == selected_bowler]
    
    # Create line chart
    fig = px.line(df_bowler, x="season", y="economyRate")
    fig.update_layout(title=f"Economy rate trend for {selected_bowler}")
    return fig


# Define the callback
@app.callback(
    Output("team-runs-bar-chart", "figure"),
    [Input("match-dropdown", "value")]
)
def update_team_runs_chart(selected_match):
    # Filter the data by the selected match
    df_filtered = bowlingDataset[bowlingDataset["match_name"] == selected_match]

    # Get the season details for the selected match
    selected_season = df_filtered["season"].iloc[0]

    # Group the data by team and calculate the total runs conceded
    df_grouped = df_filtered.groupby("bowling_team").agg({"total_runs_conceded": "sum"}).reset_index()

    # Create the stacked bar chart
    fig = px.bar(df_grouped, x="bowling_team", y="total_runs_conceded", color="bowling_team")

    # Set the chart title and axis labels
    fig.update_layout(
        title="Breakdown of runs conceded by each team in {} ({})".format(selected_match, selected_season),
        xaxis_title="Team",
        yaxis_title="Total Runs Conceded"
    )

    return fig


# Define the callback
@app.callback(
    Output("bowler-heatmap", "figure"),
    [Input("bowler-dropdown1", "value")]
)
def update_bowler_heatmap(selected_bowler):
    # Filter the data by the selected bowler
    df_filtered = bowlingDataset[bowlingDataset["fullName"] == selected_bowler]

    # Group the data by team and wickets taken
    df_grouped = df_filtered.groupby(["home_team", "wickets"]).size().reset_index(name="count")

    # Pivot the data to create a matrix of wickets taken by each team
    df_pivot = df_grouped.pivot(index="wickets", columns="home_team", values="count")

    # Create the heatmap
    fig = go.Figure(data=go.Heatmap(
        z=df_pivot.values,
        x=df_pivot.columns,
        y=df_pivot.index,
        colorscale="Blues",
        colorbar=dict(title="Frequency"),
    ))

    # Set the chart title and axis labels
    fig.update_layout(
        title="Frequency of wickets taken by " + selected_bowler + " against different teams",
        xaxis_title="Team",
        yaxis_title="Wickets taken"
    )

    return fig

