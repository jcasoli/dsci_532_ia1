from dash import Dash, html, dcc, Input, Output
import altair as alt
from vega_datasets import data

# Read in global data
cars = data.cars()

# Setup app and layout/frontend
app = Dash(__name__,  external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
server = app.server

app.layout = html.Div([
    html.Iframe(
        id='scatter',
        style={'border-width': '0', 'width': '100%', 'height': '400px'}),
    dcc.Dropdown(
        id='origin-widget',
        value='USA',  # REQUIRED to show the plot on the first page load
        options=['USA', 'Europe', 'Japan'])])

# Set up callbacks/backend
@app.callback(
    Output('scatter', 'srcDoc'),
    Input('origin-widget', 'value'))
def plot_altair(origin):
    chart = alt.Chart(cars[cars["Origin"] == origin]).mark_point().encode(
        x='Horsepower',
        y='Miles_per_Gallon',
        tooltip='Horsepower').interactive()
    return chart.to_html()

if __name__ == '__main__':
    app.run_server(debug=True)