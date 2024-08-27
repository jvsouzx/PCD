# API REST

Implementação de uma API REST simples em Python com as operações CRUD.

1. Configuração
    - Crie um ambiente virtual
    - Instale a biblioteca `Flask`
2. Implementação
    - POST
        ```python
        @app.route('/items', methods=['POST'])
        def create_item():
            data = load_data()
            new_item = request.json
            data.append(new_item)
            save_data(data)
            return jsonify(new_item), 201
        ``` 
    - GET
        ```python
        @app.route('/items', methods=['GET'])
        def get_items():
            data = load_data()
            return jsonify(data)
        ```
    - PUT
        ```python
        @app.route('/items/<int:item_id>', methods=['PUT'])
        def update_item(item_id):
            data = load_data()
            item = next((i for i in data if i['id'] == item_id), None)
            if item:
                item.update(request.json)
                save_data(data)
                return jsonify(item)
            return jsonify({'message': 'Item não encontrado'}), 404
        ``` 
    - DELETE
        ```python
        @app.route('/items/<int:item_id>', methods=['DELETE'])
        def delete_item(item_id):
            data = load_data()
            item = next((i for i in data if i['id'] == item_id), None)
            if item:
                data.remove(item)
                save_data(data)
                return jsonify({'message': 'Item deletado'})
            return jsonify({'message': 'Item não encontrado'}), 404

        ``` 
3. Teste 
    
    Execute o arquivo `main.py`, em outro terminal, na pasta do projeto execute o arquivo `test.py`
     
