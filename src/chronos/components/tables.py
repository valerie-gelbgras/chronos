# Copyright (C) 2022 Valerie GELBGRAS vgelbgra@gmail.com

from cgitb import enable
from dash import dash, html, Input, Output, State, callback_context, dash_table
import dash_bootstrap_components as dbc

from . import ids


table_header = [
    html.Thead(html.Tr([html.Th("Lap #"), html.Th("Time")]))
]

row1 = html.Tr([html.Td("Arthur"), html.Td("Dent")])
row2 = html.Tr([html.Td("Ford"), html.Td("Prefect")])
row3 = html.Tr([html.Td("Zaphod"), html.Td("Beeblebrox")])
row4 = html.Tr([html.Td("Trillian"), html.Td("Astra")])

table_body = [html.Tbody([row1, row2, row3, row4])]

# table = dbc.Table(table_header + table_body, id=ids.LAPS_TABLE, bordered=True)
table = dbc.Table(id=ids.LAPS_TABLE, bordered=True)

def get_laps_table():
    return table

def get_laps_table_header():
    return [html.Thead(html.Tr([html.Th("Lap #"), html.Th("Time")]))]

def get_new_lap_row(n_click, time):
    row = html.Tr([html.Td(str(n_click)), html.Td(time)])
    body = html.Tbody([row])
    return [body]
