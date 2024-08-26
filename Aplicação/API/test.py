import requests

URL = "http://127.0.0.1:5000/items"

def test_create_item():
    new_item = {
        "id": 1,
        "name": "Item 1",
        "description": "Descrição do Item 1"
    }
    response = requests.post(URL, json=new_item)
    print(f"POST Status Code: {response.status_code}")
    print("Response:", response.json())

def test_get_items():
    response = requests.get(URL)
    print(f"GET Status Code: {response.status_code}")
    print("Response:", response.json())


def test_update_item(item_id):
    updated_item = {
        "name": "Item 1 - Atualizado",
        "description": "Descrição do Item 1 - Atualizada"
    }
    response = requests.put(f"{URL}/{item_id}", json=updated_item)
    print(f"PUT Status Code: {response.status_code}")
    print("Response:", response.json())

def test_delete_item(item_id):
    response = requests.delete(f"{URL}/{item_id}")
    print(f"DELETE Status Code: {response.status_code}")
    print("Response:", response.json())

print("Criando um novo item:")
test_create_item()
print("\nRecuperando todos os itens:")
test_get_items()
print("\nAtualizando o item com ID 1:")
test_update_item(1)
print("\nDeletando o item com ID 1:")
test_delete_item(1)
print("\nRecuperando todos os itens após deletar")
test_get_items()