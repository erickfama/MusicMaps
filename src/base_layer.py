# Imports
import __init__
from conf import TEMPLATES_PATH
from flask import Flask, render_template, jsonify
from data.top_artists import top_artists_by_state  # Use relative import

app = Flask(__name__, template_folder=TEMPLATES_PATH)

# Approximate coordinates for Mexican states
state_coordinates = {
    "Aguascalientes": [21.8818, -102.2916],
    "Baja California": [30.8406, -115.2838],
    "Baja California Sur": [26.0444, -111.6661],
    "Campeche": [19.8301, -90.5349],
    "Chiapas": [16.7569, -93.1292],
    "Chihuahua": [28.6353, -106.0889],
    "Coahuila": [27.0587, -101.7068],
    "Colima": [19.2452, -103.7241],
    "Durango": [24.0277, -104.6532],
    "Guanajuato": [21.0190, -101.2574],
    "Guerrero": [17.4392, -99.5451],
    "Hidalgo": [20.0911, -98.7624],
    "Jalisco": [20.6595, -103.3494],
    "México": [19.4969, -99.7233],
    "Michoacán": [19.5665, -101.7068],
    "Morelos": [18.6813, -99.1013],
    "Nayarit": [21.7514, -104.8455],
    "Nuevo León": [25.5922, -99.9962],
    "Oaxaca": [17.0732, -96.7266],
    "Puebla": [19.0414, -98.2063],
    "Querétaro": [20.5888, -100.3899],
    "Quintana Roo": [19.1817, -88.4791],
    "San Luis Potosí": [22.1565, -100.9855],
    "Sinaloa": [25.0000, -107.5000],
    "Sonora": [29.2972, -110.3309],
    "Tabasco": [17.8409, -92.6189],
    "Tamaulipas": [23.7369, -99.1411],
    "Tlaxcala": [19.3139, -98.2404],
    "Veracruz": [19.1738, -96.1342],
    "Yucatán": [20.7099, -89.0943],
    "Zacatecas": [22.7709, -102.5832],
    "Mexico City": [19.4326, -99.1332]  # Added Mexico City
}

# Custom text data with coordinates for Mexican states
custom_text = {
    state: {
        "text": f"Top artist: {artist}",
        "coords": state_coordinates.get(state, [0, 0])  # Use [0, 0] as fallback
    }
    for state, artist in top_artists_by_state.items()
}

@app.route("/")
def home():
    return render_template("index.html")

# Add a new route for map data if needed
@app.route("/map_data")
def map_data():
    # You can add logic here to return map data as JSON
    return {"lat": 51.505, "lon": -0.09}  # Example coordinates for London

@app.route("/custom_text")
def get_custom_text():
    return jsonify(custom_text)

if __name__ == "__main__":
    app.run(debug=True)
