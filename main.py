from dash import Dash, html 
import dash_bootstrap_components as dbc
from layout import create_layout
from data.utill import get_olympic_data
import os

PATH = os.path.join(os.getcwd(), "data/athlete_events.csv")


def main():
    data = get_olympic_data(PATH)
    app = Dash(external_stylesheets= [dbc.themes.COSMO])
    app.title = "The Olympics"
    app.layout = create_layout(app,data)
    app.run_server(debug=True)

if __name__ == '__main__':
    main()