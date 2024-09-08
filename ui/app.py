from flask import Flask, render_template
import psycopg2
import plotly.graph_objs as go
import plotly.io as pio

app = Flask(__name__)

# Database configuration
DB_HOST = 'postgres'
DB_NAME = 'sensor_data'
DB_USER = 'userkafka'
DB_PASS = 'password'

# Function to get sensor data from the database
def get_sensor_data():
    conn = psycopg2.connect(dbname=DB_NAME, host=DB_HOST, user=DB_USER, password=DB_PASS)
    cur = conn.cursor()
    cur.execute("SELECT timestamp, temperature, humidity FROM sensor_data ORDER BY timestamp DESC LIMIT 100;")
    rows = cur.fetchall()
    conn.close()
    return rows

# Function to create a temperature graph using Plotly
def create_temperature_graph(data):
    timestamps = [row[0] for row in data]
    temperatures = [row[1] for row in data]
    
    trace = go.Scatter(x=timestamps, y=temperatures, mode='lines', name='Temperature')
    layout = go.Layout(title='Temperature over Time', xaxis=dict(title='Timestamp'), yaxis=dict(title='Temperature (°C)'))
    fig = go.Figure(data=[trace], layout=layout)

    # Render the Plotly graph to HTML
    return pio.to_html(fig, full_html=False)

# Function to create a humidity graph using Plotly
def create_humidity_graph(data):
    timestamps = [row[0] for row in data]
    humidity = [row[2] for row in data]
    
    trace = go.Scatter(x=timestamps, y=humidity, mode='lines', name='Humidity')
    layout = go.Layout(title='Humidity over Time', xaxis=dict(title='Timestamp'), yaxis=dict(title='Humidity (%)'))
    fig = go.Figure(data=[trace], layout=layout)

    # Render the Plotly graph to HTML
    return pio.to_html(fig, full_html=False)

# Flask route to display sensor data and graphs
@app.route('/')
def index():
    data = get_sensor_data()
    temperature_graph = create_temperature_graph(data)
    humidity_graph = create_humidity_graph(data)
    return render_template('index.html', temperature_graph=temperature_graph, humidity_graph=humidity_graph)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
