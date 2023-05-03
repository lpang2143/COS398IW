from dash import html, register_page

register_page(
    __name__,
    name='All Layers',
    top_nav=True,
    path='/graph_layers'
)


def layout():
    html.H2('Graphs of All Data Layers', style={'textAlign': 'center'}),
    layout = html.Div([
        html.Iframe(id="map", 
            srcDoc = open("god_map.html", "r").read(), 
            width = "100%",
            height = "512"),
    ])
    return layout