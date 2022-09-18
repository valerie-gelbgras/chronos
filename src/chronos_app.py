from dash import dash, html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets =[dbc.themes.DARKLY])


app.layout = html.Div([
    html.Div([
        html.Button('Start simulation', id='submit-val', n_clicks=0)
        ])
    ])


if __name__ == '__main__':
    app.run_server(debug=True)