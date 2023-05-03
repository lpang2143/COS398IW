from dash import html, register_page

register_page(
    __name__,
    name='Poverty and Uninsured Rate X Overdose Death Rate',
    top_nav=True,
    path='/povertyuninsured_overdose'
)


def layout():
    layout = html.Div([
        html.H2('Poverty/Uninsured Rate and Overdose Death Rate', style={'textAlign': 'center'}),
        html.Iframe(id="map", 
            srcDoc = open("poverty_uninsured.html", "r").read(), 
            width = "50%",
            height = "512"),
        html.Iframe(id="map", 
            srcDoc = open("overdose.html", "r").read(),  
            width = "50%",
            height = "512")
    ])
    return layout