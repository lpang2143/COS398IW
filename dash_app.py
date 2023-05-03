import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from navbar import create_navbar

TITLE = "Dash Visualization"
NAV = create_navbar()
# You can import icons but I wanted to keep the implementation as simple as possible
# FA = "https://use.fontawesome.com/releases/v6.2.1/css/all.css"


dash_app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets = [
        dbc.themes.MINTY,
        # FA,
    ],
    title=TITLE,
    use_pages=True,
)

'''
<!DOCTYPE html>
<html>
    <head>
        {{%metas%}}
        <title>{APP_TITLE}</title>
        {{%favicon%}}
        {{%css%}}
    </head>
    <body>
        {{%app_entry%}}
        <footer>
            {{%config%}}
            {{%scripts%}}
            {{%renderer%}}
        </footer>
        
    </body>
</html>
'''

dash_app.layout = dcc.Loading(
    id='loading_page_content',
    children=[
        html.Div(
            [
                NAV,
                dash.page_container
            ]
        )
    ],
    color='primary',
    fullscreen=True
)

server = dash_app.server

if __name__ == '__main__':
    dash_app.run_server(debug=False)