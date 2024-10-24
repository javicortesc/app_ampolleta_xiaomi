from flask import Flask, request, jsonify
from yeelight import Bulb

app = Flask(__name__)

# Sustituye la IP y el Token de tu bombilla
bulb = Bulb("192.168.0.13", port=55443)

@app.route('/turn_on', methods=['GET'])
def turn_on():
    bulb.turn_on()
    return jsonify({"status": "Bombilla Encendida"})

@app.route('/turn_off', methods=['GET'])
def turn_off():
    bulb.turn_off()
    return jsonify({"status": "Bombilla apagada"})

@app.route('/set_color/<int:red>/<int:green>/<int:blue>', methods=['GET'])
def set_color(red, green, blue):
    bulb.set_rgb(red, green, blue)
    return jsonify({"status": "Color cambiado"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)