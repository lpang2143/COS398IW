from dash import html, register_page

register_page(
    __name__,
    name='Facilities X Overdose Death Rate',
    top_nav=True,
    path='/facilities_overdose'
)


def layout():
    layout = html.Div([
        html.H2('Facilities and Overdose Death Rate', style={'textAlign': 'center'}),
        html.Iframe(id="map", 
            srcDoc = open("facilities.html", "r").read(), 
            width = "50%",
            height = "512"),
        html.Iframe(id="map", 
            srcDoc = open("overdose.html", "r").read(),  
            width = "50%",
            height = "512")
    ])
    return layout