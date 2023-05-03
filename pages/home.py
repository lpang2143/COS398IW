
from dash import html, register_page

register_page(
    __name__,
    name='Home',
    top_nav=True,
    path='/'
)


def layout():
    herve = 'assets/herve.png'
    aria = 'assets/aria.png'
    louis = 'assets/louis.png'
    layout = html.Div([
        html.Br(),
        html.H2(["Understanding the Effects of Diversity on Health Outcomes in New York City:"]),
        html.H3("Overdose and Gun Violence", style={"font-weight": "bold"}),
        html.Br(),
        html.Div([
            html.H4("Introduction", style={'font-weight': 'bold'}),
            html.P('Welcome to the visualization page for our Junior independent work. This dash application represents the work of three Juniors over the course of our COS398 Independent Work Semester. Please feel free to play around with our visualizations and toggle through the graphs.'),
            html.Div([
                html.Div([
                    html.Img(src='assets\overdose2017_chemdep.png', style={'width': '50%'})
                ]),
                html.Br(),
                html.Div([
                    html.H4("Abstract", style={'font-weight': 'bold', }),
                    html.P("New York City is one of the most diverse cities in the entire United States. But how does this diversity affect health equity within the city? That's the question that my group and I have attempted to tackle over the semester. Prevailing data appears to show that Black and Hispanic New Yorkers experience higher rates of premature death due to chronic illnesses, childbirth, and violence. The goal of our project is to investigate these disparities and study how urban diversity affects many health outcomes for underrepresented communities across New York City's boroughs by pinpointing some of the factors, such as health care access, air quality, and race, which could affect healthcare outcomes. To accomplish this, we compiled public health data into a demonstrative visualization of health outcomes and health factors in New York City. Compiling these studies, we’ll be left with a broad overview of how social factors affect health outcomes for everyday New Yorkers. Our hope is that a visualization similar to this one - lightweight, deployable, and built on free software - could be used to help inform future policy decisions. While the visualization is effective in some respects, it fails to provide useful correlative conclusions when not enough data is provided for a certain outcome or factor. "),
                ], style={'display': 'inline-block'}),
            ]),
            html.H4("Meet the Team", style={'font-weight': 'bold'}),
        ], style = {'textAlign': 'center'}),
        html.Div([
            html.Img(src=herve, style={'width': '10%', 'display': 'inline-block'}),
            html.Img(src=aria, style={'width': '10%', 'display': 'inline-block'}),
            html.Img(src=louis, style={'width': '10%', 'display': 'inline-block'}),
            html.P("From left to right: Herve Ishimwe, Aria Nagai, Louis Pang. We're three computer science students at Princeton looking to learn more about the intersection between public health and computer science.")
        ] ,style={'textAlign': 'center'}),
    ])
    return layout