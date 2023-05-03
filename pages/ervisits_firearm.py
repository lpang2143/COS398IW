from dash import html, register_page

register_page(
    __name__,
    name='ER Visits Opioid OD X Firearm Death Rate',
    top_nav=True,
    path='/ervisits_firearm'
)


def layout():
    layout = html.Div([
        html.H2('ER Visits due to Opioid OD and Firearm Death Rate', style={'textAlign': 'center'}),
        html.Iframe(id="map", 
            srcDoc = open("overdose_hospitalizations.html", "r").read(), 
            width = "50%",
            height = "512"),
        html.Iframe(id="map", 
            srcDoc = open("gun_deaths.html", "r").read(),  
            width = "50%",
            height = "512")
    ])
    return layout