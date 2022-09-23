from turtle import width
from dash import html, Input, Output
import dash_bootstrap_components as dbc
from chronos_app import app

start_button_style = {'background-color': 'green',
                    'color': 'white',
                    'height': '50px',
                    'width': '200px'}

stop_button_style = {'background-color': 'red',
                    'color': 'white',
                    'height': '50px',
                    'width': '200px'}

def get_start_stop_button():
    return html.Button('Start', id='submit-val', n_clicks=0, style=start_button_style)


@app.callback(
    [Output('submit-val', 'children'),
     Output('submit-val', 'style')],
    [Input('submit-val', 'n_clicks')]
)
def update_output(n_clicks):
    if n_clicks % 2:
        return ["Stop", stop_button_style]
    return ["Start", start_button_style]
