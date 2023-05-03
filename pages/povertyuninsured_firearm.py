from dash import html, register_page

register_page(
    __name__,
    name='Poverty and Uninsured Rate X Firearm Death Rate',
    top_nav=True,
    path='/povertyuninsured_firearm'
)


def layout():
    layout = html.Div([
        html.H2('Poverty/Uninsured Rate and Firearm Death Rate', style={'textAlign': 'center'}),
        html.Iframe(id="map", 
            srcDoc = open("poverty_uninsured.html", "r").read(), 
            width = "50%",
            height = "512"),
        html.Iframe(id="map", 
            srcDoc = open("gun_deaths.html", "r").read(),  
            width = "50%",
            height = "512")
    ])
    return layout