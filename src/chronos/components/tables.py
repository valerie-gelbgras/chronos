# Copyright (C) 2022 Valerie GELBGRAS vgelbgra@gmail.com

from dash import html
import dash_bootstrap_components as dbc

from . import ids


def get_laps_table():
    return dbc.Table(id=ids.LAPS_TABLE, bordered=True)


def get_laps_table_header():
    return [html.Thead(html.Tr([html.Th("Lap #"), html.Th("Time")]))]


def get_new_lap_row(n_click, time):
    row = html.Tr([html.Td(str(n_click)), html.Td(time)])
    body = html.Tbody([row])
    return [body]
