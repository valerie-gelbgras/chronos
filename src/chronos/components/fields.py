# Copyright (C) 2022 Valerie GELBGRAS vgelbgra@gmail.com

from dash import html, Input, Output
import dash_bootstrap_components as dbc
from dash import dcc
from chronos_app import app
from . import ids
from . import styles
from time_interval import TimeInterval


def get_timer_field():
    return html.Div([
                    dbc.Alert(id=ids.TIMER_DISPLAY, color="light", style=styles.BUTTON_SIZE),
                    dcc.Interval(id=ids.INTERVAL, interval=50, n_intervals=0)
                    ])


@app.callback(
    Output(ids.TIMER_DISPLAY, 'children'),
    [Input(ids.INTERVAL, 'n_intervals'),
     Input(ids.INTERVAL, 'interval')])
def update_interval(interval_count, interval_size_in_milliseconds):
    try:
        return str(TimeInterval.from_milliseconds(interval_count * interval_size_in_milliseconds))
    except:
        return str(TimeInterval.from_milliseconds(0))
