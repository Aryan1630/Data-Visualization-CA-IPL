import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objs as go
import dash
from dash import dcc
from app import app
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from dash import html



winnerList = pd.read_csv(r"all_season_summary.csv")
winnerList.head()

winnersFilter = winnerList[winnerList['description'].str.startswith('Final')]
winner = winnersFilter['winner'].value_counts()
colors = ['#1F97FA', '#ECF024', '#FF8000','#A600FF','#0662B0', '#2E348C']
winnerfig = px.bar(winner)
winnerfig.update_traces(marker_color=colors)
winnerfig.update_layout(
    xaxis_title="teams",
    yaxis_title="Number of titles"
) 

columns_to_drop = ['name','1st_inning_score','2nd_inning_score','home_score','away_score','result','start_date','end_date','venue_id','venue_name','home_captain','away_captain',"pom","points","super_over","home_overs","away_overs","highlights","home_key_batsman","home_key_bowler","home_playx1","away_playx1","away_key_batsman","away_key_bowler","match_days","umpire1","umpire2","tv_umpire","referee","reserve_umpire"]
newDataset = winnerList.drop(columns_to_drop, axis = 1)
grouped_by_season_home = newDataset.groupby(['season', 'home_team'])
season_home_runs = grouped_by_season_home['home_runs'].sum()

# Reset index to turn the groupby result into a DataFrame
season_home_runs_df = season_home_runs.reset_index()

# Create a dropdown list of seasons
seasons = sorted(season_home_runs_df['season'].unique())
season_dropdown = [{'label': season, 'value': season} for season in seasons]


toss_loss_match_win = winnerList[(winnerList['toss_won'] != winnerList['winner'])].shape[0]
toss_win_match_win = winnerList[(winnerList['toss_won'] == winnerList['winner'])].shape[0]

percentage_match_won = toss_win_match_win / winnerList.shape[0] * 100
percentage_match_lost = toss_loss_match_win / winnerList.shape[0] * 100

totalRuns = int(winnerList['home_runs'].sum() + winnerList['away_runs'].sum())

totalBoundaries = int(winnerList['home_boundaries'].sum() + winnerList['away_boundaries'].sum())


#venue filters
groupedBySeason_Venues = winnerList.groupby(['season','venue_name'])
groupedBySeason_Venues = winnerList.groupby(['season', 'venue_name']).size().reset_index(name='counts')

# Create a dropdown with the available seasons
seasons = groupedBySeason_Venues['season'].unique()
season_dropdown = [{'label': str(season), 'value': season} for season in seasons]



venueCounts = winnerList['venue_name'].nunique()


team_stats = winnerList.groupby(['season', 'home_team']).agg({
    'home_runs': 'sum'
}).reset_index()


# team_season_wins = pd.DataFrame(columns=['season', 'team', 'wins'])
# for name, group in winnerList.groupby(['season', 'winner']):
#     season = name[0]
#     team = name[1]
#     wins = len(group)
#     team_season_wins = team_season_wins.append({'season': season, 'team': team, 'wins': wins}, ignore_index=True)

team_season_wins = pd.DataFrame(columns=['season', 'team', 'wins'])
for name, group in winnerList.groupby(['season', 'winner']):
    season = name[0]
    team = name[1]
    wins = len(group)
    team_season_wins = team_season_wins.append({'season': season, 'team': team, 'wins': wins}, ignore_index=True)


#app initialized
#app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, 'assets/style.css', "https://fonts.googleapis.com/css2?family=Yeseva+One&family=Oswald&family=Bruno+Ace+SC&display=swap"], external_scripts=['assets/main.js'])



#firstContainer start
firstContent = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.Div([
                html.H5("Summary of Matches from", className="sidebar"),
                html.H4("2008-2022", className="sidebar-years"),
                html.Div([
                    html.H2('', id="count"),
                    html.P("Matches"),
                    html.Div([
                        html.H4(f'{venueCounts}'),
                        html.P("Total Venues")
                    ], className="matchesTotals"),
                ], className="matchCounter"),
            ], className="matchCounter"),
        ], width=2),
        dbc.Col([
            html.H4("Total Number of Titles win by teams", className="text-center graphHeader"),
            html.Div([
                dcc.Graph(
                    id='bar-graph',
                    figure=winnerfig
                )
            ], className="winnerFigure")
        ], width=5, className="smallgraphCols"),
        
        dbc.Col([
            html.H4("Percentage of Matches Won/Lost if Toss is Won", className="text-center graphHeader"),
            dcc.Graph(
                id='pie-chart',
                figure=go.Figure(data=[go.Pie(
                    labels=['% of Matches Won if Toss is Won', '% of Matches Lost if Toss is Won'],
                    values=[percentage_match_won, percentage_match_lost],
                    hole=0.3
                )], layout=go.Layout(
                    title='')
                ),style={'height': '500px', 'width': '500px'})
            ], width=5)
        ])
    ], className="text-center")


#first container end


#second Container start


secondContainer = html.Div([
    dbc.Container([
        html.H1("Team And Venue stats with respective season", className="text-center scontainerHeader"),
        dbc.Row([
            dbc.Col([
                 html.H4("Number of Matches won by every team/season", className="text-center venueHeader"),
                 html.Div([ dcc.Dropdown(
        id='season-dropdown',
        options=[{'label': s, 'value': s} for s in team_season_wins['season'].unique()],
        value=team_season_wins['season'].iloc[0]
    ),
    dcc.Graph(id='wins-graph')
    ],className="sgraphContainer"),
               

            ], width=6),
            dbc.Col([
                html.H4("Venue Details", className="text-center venueHeader"),
                html.Div([
                    html.Div([
                        # dcc.Dropdown(
                        #     id='season-dropdown',
                        #     options=season_dropdown,
                        #     value=seasons[0]
                        # )
                ], style={'width': '200px'}),
                dcc.Graph(id='season-venues-plot')
                ],className="sgraphContainer")
            ], width=6)            
        ])
    ]),
], className="osecondContainer")

#second container end here
#third container start here
thirdContainer = html.Div([
    dbc.Container([
        dbc.Row([
            html.H4("Toss Details", className="text-center tossHeader"),
            dbc.Col([
                
                dcc.Graph(id="toss-graph")
            ],width = 6, className="thirdContainerCol1"),
            dbc.Col([
                html.Div([
    dcc.Graph(id='captains-graph')
])
            ])
        ])
    ])
], className="thirdContainer")

#third Container end here


#fourthContent start here 

fourthContent = html.Div([
    dbc.Container([
         dcc.Graph(
        id='team-performance-chart'
    )
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

#fourthContent end here

#footer start here 
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

#footer end here


layout = html.Div([
    firstContent,
    secondContainer,
    thirdContainer,
    fourthContent,
    fifthContent,
    footer

])

# Define the callbacks to update the graphs
@app.callback(
    Output('wins-graph', 'figure'),
    [Input('season-dropdown', 'value')]
)
def update_wins_graph(season):
    filtered_data = team_season_wins[team_season_wins['season'] == season]
    fig = px.bar(filtered_data, x='team', y='wins', title=f'Wins by Team in {season}')
    return fig





@app.callback(
    Output('season-venues-plot', 'figure'),
    [Input('season-dropdown', 'value')]
)
def update_season_venues_plot(selected_season):
    # Filter the data by the selected season
    season_data = groupedBySeason_Venues[groupedBySeason_Venues['season'] == selected_season]

    # Create the plot using Plotly
    fig = px.bar(season_data, x='venue_name', y='counts', title=f'Counts of Venues in {selected_season}')
    fig.update_xaxes(title='Venue Name')
    fig.update_yaxes(title='Counts')
    fig.update_layout(barmode='group')
    return fig





@app.callback(
    Output('toss-graph', 'figure'),
    [Input('season-dropdown', 'value')]
)
def update_toss_graph(selected_season):
    # Group the data by season and toss winner and count the occurrences
    toss_counts = winnerList.groupby(['season', 'toss_won']).size().reset_index(name='toss_count')

    # Filter the data by the selected season
    toss_counts = toss_counts[toss_counts['season'] == selected_season]

    # Sort the data by toss count in descending order
    toss_counts = toss_counts.sort_values('toss_count', ascending=False)

    # Keep only the top 5 teams
    toss_counts = toss_counts.head(5)

    # Create the plot using Plotly
    fig = px.bar(toss_counts, x='toss_won', y='toss_count', title=f'Teams with Most Toss Wins in {selected_season}')
    fig.update_xaxes(title='Team')
    fig.update_yaxes(title='Toss Count')
    fig.update_layout(barmode='group')
    return fig






# Define the app callbacks for Captain data
@app.callback(
    Output('captains-graph', 'figure'),
    [Input('season-dropdown', 'value')]
)
def update_wins_graph(season):
    filtered_data = winnerList[winnerList['season'] == season]
    captain_wins = filtered_data.groupby('home_captain')['winner'].apply(lambda x: x[x == x.mode()[0]].count())
    captain_wins = captain_wins.sort_values(ascending=False)
    fig = px.bar(x=captain_wins.index, y=captain_wins.values, title=f'Successful Captains as per {season}')
    fig.update_xaxes(title='Captain Name')
    fig.update_yaxes(title='Number of Wins')
    return fig



@app.callback(
    dash.dependencies.Output('team-performance-chart', 'figure'),
    [dash.dependencies.Input('season-dropdown', 'value')]
)
def update_team_performance_chart(selected_season):
    # Filter the data based on the selected season
    filtered_team_stats = team_stats[team_stats['season'] == selected_season]

    # Create the line chart
    fig = px.line(filtered_team_stats, x='home_team', y='home_runs')

    # Set the chart title and axis labels
    fig.update_layout(title='Team Performance in Season {}'.format(selected_season),
                      xaxis_title='Home Team',
                      yaxis_title='Total Runs')

    # Return the chart
    return fig

# if __name__ == '__main__':
#     app.run_server(debug=True)
