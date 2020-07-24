import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('SimpleExample', external_stylesheets=external_stylesheets)


app.layout = html.Div([
    html.H1('TTTTTTT', style={'margin-top': 10}),
    dcc.Graph(id='slider-graph', animate=True, style={"backgroundColor": "#1a2d46", 'color': '#ffffff'}),
    dcc.Slider(
        id='slider-updatemode',
        marks={i: '{}'.format(i) for i in range(20)},
        max=20,
        value=2,
        step=1,
        updatemode='drag',
    ),
])


@app.callback(
               Output('slider-graph', 'figure'),
              [Input('slider-updatemode', 'value')])
def display_value(value):


    x = []
    for i in range(value):
        x.append(i)

    y = []
    for i in range(value):
        y.append(i)

    graph = [
                {'x': [1, 2, value], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [value, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'Montréal'},
            ]
    layout = {
                'title': 'Dash Data Visualization'
            }
    return {'data': graph, 'layout': layout}