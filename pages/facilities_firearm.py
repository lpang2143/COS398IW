from dash import html, register_page

register_page(
    __name__,
    name='Facilities X Firearm Death Rate',
    top_nav=True,
    path='/facilities_firearm'
)


def layout():
    layout = html.Div([
        html.H2('Facilities and Firearm Death Rate', style={'textAlign': 'center'}),
        html.Iframe(id="map", 
            srcDoc = open("facilities.html", "r").read(), 
            width = "50%",
            height = "512"),
        html.Iframe(id="map", 
            srcDoc = open("gun_deaths.html", "r").read(),  
            width = "50%",
            height = "512")
    ])
    return layout