from dash import Dash, html
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeChangerAIO
import bar_chart, countries

def create_layout(app, data):
    header = html.H1("The Olympics")
    return dbc.Container(children = [
        header,
        dbc.Row(
            [
                dbc.Col([
                    countries.render(app,data),
                ], width=4),
                dbc.Col([bar_chart.render(app,data),], width=8)
            ]
        )
   ],fluid=True,className="dbc")