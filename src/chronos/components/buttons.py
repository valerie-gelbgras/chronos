# Copyright (C) 2022 Valerie GELBGRAS vgelbgra@gmail.com

from dash import dash, html, Input, Output, State, callback_context
import dash_bootstrap_components as dbc

from chronos_app import app
from . import ids
from . import styles
from .state_color import StateColor


def get_start_stop_button():
    return html.Div([dbc.Button(StateColor.PAUSE.name, id=ids.START_BUTTON, n_clicks=0, style=styles.BUTTON_SIZE, color=StateColor.START.value)])


def get_reset_button():
    return html.Div([dbc.Button(StateColor.RESET.name, id=ids.RESET_BUTTON, n_clicks=0, style=styles.BUTTON_SIZE, color=StateColor.RESET.value)])


def get_laps_button():
    return html.Div([dbc.Button(StateColor.LAPS.name, id=ids.LAPS_BUTTON, n_clicks=0, style=styles.BUTTON_SIZE, color=StateColor.LAPS.value)])


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
    elif not user_click or user_click == ids.RESET_BUTTON or user_click== ids.LAPS_BUTTON:
        return update_when_reset_button_is_clicked()


def update_when_start_button_is_clicked(start_button_status):
    if start_button_status == StateColor.START.name:
        return StateColor.PAUSE.name, StateColor.PAUSE.value, False, dash.no_update
    return StateColor.START.name, StateColor.START.value, True, dash.no_update


def update_when_reset_button_is_clicked():
    return StateColor.START.name, StateColor.START.value, True, 0


# @app.callback(
#     [Output(ids.START_BUTTON, 'children'),
#      Output(ids.START_BUTTON, 'color'),
#      Output(ids.INTERVAL, 'disabled'),
#      Output(ids.INTERVAL, 'n_intervals')],
#     [Input(ids.START_BUTTON, 'n_clicks'),
#      Input(ids.RESET_BUTTON, 'n_clicks')],
#      State(ids.LAPS_TABLE, 'children')
# )
# def update(n_clicks_start, n_click_reset, start_button_status):
#     user_click = callback_context.triggered[0]['prop_id'].split('.')[0]
#     if user_click == ids.START_BUTTON:
#         return update_when_start_button_is_clicked(start_button_status)
#     elif not user_click or user_click == ids.RESET_BUTTON or user_click== ids.LAPS_BUTTON:
#         return update_when_reset_button_is_clicked()
