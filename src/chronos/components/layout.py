# Copyright (C) 2022 Valerie GELBGRAS vgelbgra@gmail.com

from dash import html
import dash_bootstrap_components as dbc

from .buttons import get_start_stop_button, get_reset_button, get_laps_button
from .fields import get_timer_field

body = dbc.Container(
    [
        dbc.Row([
            dbc.Col(get_start_stop_button()), 
                dbc.Col(get_timer_field()),
                dbc.Col([
                    get_reset_button(),
                    html.Br(),
                    get_laps_button()
                    ])
            ], 
            justify="center",
            align="top",
            class_name="h-100"
            ),
        ],
    style={"height": "100vh"}
    )


def get_layout():
    return html.Div(
        [
            html.Div([body])
        ])