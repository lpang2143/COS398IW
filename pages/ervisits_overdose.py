from dash import html, register_page

register_page(
    __name__,
    name='ER Visits Opioid OD X Overdose Death Rate',
    top_nav=True,
    path='/ervisits_overdose'
)


def layout():
    layout = html.Div([
        html.H2('ER Visits due to Opioid OD and Overdose Death Rate', style={'textAlign': 'center'}),
        html.Iframe(id="map", 
            srcDoc = open("overdose_hospitalizations.html", "r").read(), 
            width = "50%",
            height = "512"),
        html.Iframe(id="map", 
            srcDoc = open("overdose.html", "r").read(),  
            width = "50%",
            height = "512")
    ])
    return layout