from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route('/')
def home():
    return 'A API está online!'

def load_data():
    with open('data/database.json', 'r') as file:
        return json.load(file)

def save_data(data):
    with open('data/database.json', 'w') as file:
        json.dump(data, file, indent=4)

@app.route('/items', methods=['POST'])
def create_item():
    data = load_data()
    new_item = request.json
    data.append(new_item)
    save_data(data)
    return jsonify(new_item), 201

@app.route('/items', methods=['GET'])
def get_items():
    data = load_data()
    return jsonify(data)

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = load_data()
    item = next((i for i in data if i['id'] == item_id), None)
    if item:
        item.update(request.json)
        save_data(data)
        return jsonify(item)
    return jsonify({'message': 'Item não encontrado'}), 404

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    data = load_data()
    item = next((i for i in data if i['id'] == item_id), None)
    if item:
        data.remove(item)
        save_data(data)
        return jsonify({'message': 'Item deletado'})
    return jsonify({'message': 'Item não encontrado'}), 404

initial_data = []
save_data(initial_data)

app.run()

