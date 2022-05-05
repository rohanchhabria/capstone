from random import randint
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get():
    return jsonify({'status': '200'}), 200

@app.route('/<string:string>/', methods=['GET'])
def post(string):
    return jsonify({f'{string}': randint(0, len(string))}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000, use_reloader=True)
    