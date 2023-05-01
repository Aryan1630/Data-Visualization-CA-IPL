import dash
from app import app
import dash_bootstrap_components as dbc
from dash import html

#main Container start

container = dbc.Container([
    html.Div([
        html.Div([
        html.H1("INDIAN PREMIERE LEAGUE"),
        html.H5("ALL THE STATS FROM WINS TO LOOSE"),
        html.A("VISIT OFFICIAL WEBSITE", id="offWeb", className="btn", href="https://www.iplt20.com/"),
        ], className="containerHeader text-center"),
        html.Img(src="assets/images/Dhoni-1.png", className="containerImage")
    ])    
], className="contentContainer container")

link = html.A(
    children=html.Div(
        id="mouse-scroll",
        children=[
            html.Div(
                className="mouse",
                children=html.Div(className="mouse-in")
            ),
            html.Div(
                children=[
                    html.Span(className="down-arrow-1"),
                    html.Span(className="down-arrow-2"),
                    html.Span(className="down-arrow-3")
                ]
            )
        ]
    ),
    href="#",
    className="scrollIcon"
)

#main container end. 


#third container start
secondContent = dbc.Container([
    html.H1("TEAMS", className="text-center teams-header"),
         dbc.Row([
             dbc.Col([
                 dbc.Card(
                             [
        dbc.CardImg(src="assets/images/mi.png", top=True),
        dbc.CardBody(
            [
                html.A(
                html.H4("MUMBAI INDIANS", className="card-title text-center"),
                href="https://www.mumbaiindians.com/"
                )
            ]
        ),
    ],
    style={"width": "18rem"},
)
             ], width=4),
             dbc.Col([
                 dbc.Card(
                             [
        dbc.CardImg(src="assets/images/csk.png", top=True),
        dbc.CardBody(
            [
                html.A(
                html.H4("CHENNAI SUPER KINGS", className="card-title text-center "),
                href="https://www.chennaisuperkings.com/")
            ]
        ),
    ],
    style={"width": "18rem"},
)
             ], width=4),
             dbc.Col([
                 dbc.Card(
                             [
        dbc.CardImg(src="assets/images/kkr.png", top=True),
        dbc.CardBody(
            [
                html.A(
                html.H4("KOLKATA KNIGHT RIDERS", className="card-title text-center "),
                href="https://www.kkr.in/")
            ],
        ),
    ],
    style={"width": "18rem"},
)], width=4)
         ]),

         dbc.Row([
             dbc.Col([
                 dbc.Card(
                             [
        dbc.CardImg(src="assets/images/dc.png", top=True),
        dbc.CardBody(
            [
                html.A(
                html.H4("DELHI CAPITALS", className="card-title text-center "),
                href="https://www.delhicapitals.in/")
            ]
        ),
    ],
    style={"width": "18rem"},
)
             ], width=4),
             dbc.Col([
                 dbc.Card(
                             [
        dbc.CardImg(src="assets/images/srh.png", top=True),
        dbc.CardBody(
            [
                html.A(
                html.H4("SUNRISERS HYDERABAD", className="card-title text-center "),
                href="https://www.sunrisershyderabad.in/")
            ]
        ),
    ],
    style={"width": "18rem"},
)
             ], width=4),
             dbc.Col([
                 dbc.Card(
                             [
        dbc.CardImg(src="assets/images/PBKS.png", top=True),
        dbc.CardBody(
            [
                html.A(
                html.H4("PUNJAB KINGS XI", className="card-title text-center "),
                href="https://www.punjabkingsipl.in/")
            ],
        ),
    ],
    style={"width": "18rem"},
)], width=4)
         ], className="row2"),
         dbc.Row([
             dbc.Col([
                 dbc.Card(
                             [
        dbc.CardImg(src="assets/images/rcb.png", top=True),
        dbc.CardBody(
            [
                html.A(
                html.H4("ROYAL CHALLENGERS BANGALORE", className="card-title text-center "),
                href="https://www.royalchallengers.com/")
            ]
        ),
    ],
    style={"width": "18rem"},
)
             ], width=4),
             dbc.Col([
                 dbc.Card(
                             [
        dbc.CardImg(src="assets/images/LSG.jpg", top=True),
        dbc.CardBody(
            [
                html.A(
                html.H4("LUCKNOW SUPER GIANTS", className="card-title text-center "),
                href="https://www.lucknowsupergiants.in/")
            ]
        ),
    ],
    style={"width": "18rem"},
)
             ], width=4),
             dbc.Col([
                 dbc.Card(
                             [
        dbc.CardImg(src="assets/images/gt.png", top=True),
        dbc.CardBody(
            [
                html.A(
                html.H4("GUJRAT TITANS", className="card-title text-center "),
                href="https://www.gujarattitansipl.com/")
            ],
        ),
    ],
    style={"width": "18rem"},
)], width=4)
         ], className="row3")


], className="winnersBar container")



thirdContent = html.Div([
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
    container,
    link,
    secondContent,
    thirdContent,
    footer
])


