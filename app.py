from flask import Flask, jsonify, Response
import csv
import pandas as pd
import io
import matplotlib.pyplot as plt
import base64

app = Flask(__name__)

@app.route('/get-mean')
def get_mean():
    data = pd.read_csv('concentration.timeseries.csv')
    concentrations = data['concentration']
    mean_concentration = sum(concentrations) / len(concentrations)
    return jsonify({'mean_concentration': mean_concentration})

@app.route('/get-std-deviation')
def get_std_deviation():
    data = pd.read_csv('concentration.timeseries.csv')
    concentrations = data['concentration']
    std_deviation = pd.Series(concentrations).std()
    return jsonify({'std_deviation': std_deviation})

@app.route('/get-sum')
def get_sum():
    data = pd.read_csv('concentration.timeseries.csv')
    concentrations = data['concentration']
    total_sum = sum(concentrations)
    return jsonify({'total_sum': total_sum})

@app.route('/get-image')
def get_image():
    data = pd.read_csv('concentration.timeseries.csv')
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    x = data['x']
    y = data['y']
    z = data['z']
    concentration = data['concentration']

    sc = ax.scatter(x, y, z, c=concentration, cmap='viridis')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    fig.colorbar(sc, label='Concentration', pad=0.1)

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()

    buffer.seek(0)
    return Response(buffer.read(), content_type='image/png')

if __name__ == '__main__':
    app.run(debug=True, port=5001, host="0.0.0.0")
