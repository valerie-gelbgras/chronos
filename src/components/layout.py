from dash import dash, html
import dash_bootstrap_components as dbc

from .buttons import get_start_stop_button

body = dbc.Container(
    [
        dbc.Row(
            [
                get_start_stop_button()
            ], 
            justify="center",
            align="center",
            className="h-100")
        ],
    style={"height": "100vh"}
    )


def get_layout():
    return html.Div(
        [
            html.Div([body])
        ])