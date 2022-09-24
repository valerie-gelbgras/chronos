# Copyright (C) 2022 Valerie GELBGRAS vgelbgra@gmail.com

from enum import Enum, unique
from dash import dash, html, Input, Output, State, callback_context
import dash_bootstrap_components as dbc
from chronos_app import app
from . import ids
from . import styles


def get_start_stop_button():
    return html.Div([dbc.Button(ButtonStatus.START.value, id=ids.START_BUTTON, n_clicks=0, style=styles.BUTTON_SIZE, color='success')])


def get_reset_button():
    return html.Div([dbc.Button(ButtonStatus.RESET.value, id=ids.RESET_BUTTON, n_clicks=0, style=styles.BUTTON_SIZE, color='primary')])


def get_laps_button():
    return html.Div([dbc.Button(ButtonStatus.LAPS, id=ids.LAPS_BUTTON, n_clicks=0, style=styles.BUTTON_SIZE)])

@unique
class ButtonStatus(Enum):
    START = 'START'
    STOP = 'STOP'
    RESET = 'RESET'
    LAPS = 'LAPS'


@app.callback(
    [Output(ids.START_BUTTON, 'children'),
     Output(ids.START_BUTTON, 'color'),
     Output(ids.INTERVAL, 'disabled'),
     Output(ids.INTERVAL, 'n_intervals')],
    [Input(ids.START_BUTTON, 'n_clicks'),
     Input(ids.RESET_BUTTON, 'n_clicks')],
     State(ids.START_BUTTON, 'children')
)
def update(n_clicks_start, n_click_reset, start_button_status):
    user_click = callback_context.triggered[0]['prop_id'].split('.')[0]
    if user_click == ids.START_BUTTON:
        return update_when_start_button_is_clicked(start_button_status)
    elif not user_click or user_click == ids.RESET_BUTTON:
        return update_when_reset_button_is_clicked()


def update_when_start_button_is_clicked(start_button_status):
    if start_button_status == ButtonStatus.START.value:
        return ButtonStatus.STOP.value, "danger", False, dash.no_update
    return ButtonStatus.START.value, "success", True, dash.no_update

def update_when_reset_button_is_clicked():
    return ButtonStatus.START.value, "success", True, 0
