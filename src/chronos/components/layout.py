# Copyright (C) 2022 Valerie GELBGRAS vgelbgra@gmail.com

from dash import html
import dash_bootstrap_components as dbc

from .buttons import get_start_stop_button, get_reset_button, get_laps_button
from .fields import get_timer_field
from .tables import get_laps_table

body = dbc.Container(
    [
        html.Div(
            [
                dbc.Row(dbc.Col(html.Br())),
                dbc.Row(
                    [
                        dbc.Col([get_start_stop_button()], width={"size": 2, "offset": 3}),
                        dbc.Col([get_timer_field()], md=2),
                        dbc.Col(
                            [
                                get_reset_button(),
                                html.Br(),
                                get_laps_button()
                            ])
                    ],
                    justify="center",
                    align="top",
                    class_name="h-100"),
                html.Br(),
                dbc.Row(
                    [
                        dbc.Col([get_laps_table()], width={"size": 3})
                    ],
                    justify="center")
            ])
    ],
    style={"height": "100vh"},
    fluid=True
    )


def get_layout():
    return html.Div(
        [
            html.Div([body])
        ])
