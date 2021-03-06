import altair as alt
from dash import Dash, dcc, html, Input, Output
from vega_datasets import data

    
cars = data.cars()

def plot_altair(xmax):
    chart = alt.Chart(cars[cars['Miles_per_Gallon'] < xmax]).mark_point().encode(
        x='Miles_per_Gallon',
        y='Weight_in_lbs')
    return chart.to_html()

app = Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
server = app.server

app.layout = html.Div([
        html.Iframe(
            id='scatter',
            srcDoc=plot_altair(xmax=0),
            style={'border-width': '0', 'width': '100%', 'height': '400px'}),
        dcc.Slider(id='xslider', min=0, max=50)])
        
@app.callback(
    Output('scatter', 'srcDoc'),
    Input('xslider', 'value'))
def update_output(xmax):
    return plot_altair(xmax)

if __name__ == '__main__':
    app.run_server(debug=True)