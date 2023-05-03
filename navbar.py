from dash import html
import dash_bootstrap_components as dbc


def create_navbar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.DropdownMenu(
                nav=True,
                in_navbar=True,
                label="Menu",
                align_end=True,
                children=[  # List of all available graph combinations
                    dbc.DropdownMenuItem("Home", href='/'),
                    dbc.DropdownMenuItem("All Layers", href='/graph_layers'),
                    dbc.DropdownMenuItem(divider=True),
                    dbc.DropdownMenuItem("Air Quality X Overdose Death Rate", href='/airquality_overdose'),
                    dbc.DropdownMenuItem("ER Visits Opioid OD X Overdose Death Rate", href='/ervisits_overdose'),
                    dbc.DropdownMenuItem("Facilities X Overdose Death Rate", href='/facilities_overdose'),
                    dbc.DropdownMenuItem("Poverty and Uninsured Rate X Overdose Death Rate", href='/povertyuninsured_overdose'),
                    dbc.DropdownMenuItem("Race X Overdose Death Rate", href='/race_overdose'),
                    dbc.DropdownMenuItem(divider=True),
                    dbc.DropdownMenuItem("Air Quality X Firearm Death Rate", href='/airquality_firearm'),
                    dbc.DropdownMenuItem("Er Visits Opioid OD X Firearm Death Rate", href='/ervisits_firearm'),
                    dbc.DropdownMenuItem("Facilities X Firearm Death Rate", href='/facilities_firearm'),
                    dbc.DropdownMenuItem("Poverty and Uninsured Rate X Firearm Death Rate", href='/povertyuninsured_firearm'),
                    dbc.DropdownMenuItem("Race X Firearm Death Rate", href='/race_firearm'),
                ],
            ),
        ],
        brand='Home',
        brand_href="/",
        sticky="top",
        color="primary",
        dark=True,  # Change this to change color of text within the navbar (False for dark text)
    )

    return navbar