# Copyright (C) 2022 Valerie GELBGRAS vgelbgra@gmail.com

from dash import dash, html, Input, Output, State, callback_context
import dash_bootstrap_components as dbc

from chronos_app import app
from . import ids
from . import styles
from .state_color import StateColor
from .tables import get_laps_table_header, get_new_lap_row


def get_start_stop_button():
    return html.Div([dbc.Button(StateColor.PAUSE.state, id=ids.START_BUTTON, n_clicks=0, style=styles.BUTTON_SIZE, color=StateColor.START.color)])


def get_reset_button():
    return html.Div([dbc.Button(StateColor.RESET.state, id=ids.RESET_BUTTON, n_clicks=0, style=styles.BUTTON_SIZE, color=StateColor.RESET.color)])


def get_laps_button():
    return html.Div([dbc.Button(StateColor.LAP.state, id=ids.LAP_BUTTON, n_clicks=0, style=styles.BUTTON_SIZE, color=StateColor.LAP.color)])


@app.callback(
    [Output(ids.START_BUTTON, 'children'),
     Output(ids.START_BUTTON, 'color'),
     Output(ids.INTERVAL, 'disabled'),
     Output(ids.INTERVAL, 'n_intervals'),
     Output(ids.LAPS_TABLE, 'children'),
     Output(ids.LAP_BUTTON, 'n_clicks')],
    [Input(ids.START_BUTTON, 'n_clicks'),
     Input(ids.RESET_BUTTON, 'n_clicks'),
     Input(ids.LAP_BUTTON, 'n_clicks')],
    [State(ids.START_BUTTON, 'children'),
     State(ids.LAPS_TABLE, 'children'),
     State(ids.TIMER_DISPLAY, 'children')]
)
def update(n_clicks_start, n_clicks_reset, n_clicks_lap, start_button_state, table_state, timer_state):
    user_click = callback_context.triggered[0]['prop_id'].split('.')[0]
    if user_click == ids.START_BUTTON:
        return update_when_start_button_is_clicked(start_button_state)
    elif not user_click or user_click == ids.RESET_BUTTON:
        return update_when_reset_button_is_clicked()
    elif user_click == ids.LAP_BUTTON:
        new_table = update_table(n_clicks_lap, table_state, timer_state)
        return dash.no_update, dash.no_update, dash.no_update, dash.no_update, new_table, dash.no_update


def update_when_start_button_is_clicked(start_button_status):
    if start_button_status == StateColor.START.state:
        return StateColor.PAUSE.state, StateColor.PAUSE.color, False, dash.no_update, dash.no_update, dash.no_update
    return StateColor.START.state, StateColor.START.color, True, dash.no_update, dash.no_update, dash.no_update


def update_when_reset_button_is_clicked():
    return StateColor.START.name, StateColor.START.color, True, 0, [], 0


def update_table(n_clicks_laps, previous_table_data, time):
    if n_clicks_laps == 0:
        return []
    if previous_table_data == []:
        return get_laps_table_header() + get_new_lap_row(n_clicks_laps, time)
    return previous_table_data + get_new_lap_row(n_clicks_laps, time)
