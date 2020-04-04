import requests
url = "https://fakerestapi.azurewebsites.net/api"


# Consultar autores de un libro
def get_authors_for_book(book_id):
    endpoint = "https://fakerestapi.azurewebsites.net/authors/books/{}".format(str(book_id))
    peticion = requests.get(endpoint)
    return peticion


# Consultar listado de autores
def get_all_authors():
    endpoint = "/Authors"
    peticion = requests.get(url + endpoint)
    return peticion


# Insertar un autor
def create_author(author_id, book_id, first_name, last_name):
    endpoint = "/Authors"
    headers = {"Content-Type": "application/json"}
    payload = {
        "ID": author_id,
        "IDBook": "{}".format(book_id),
        "FirstName": "{}".format(first_name),
        "LastName": "{}".format(last_name),
    }
    peticion = requests.post(url + endpoint, data=payload, headers=headers)
    return peticion


# Eliminar un autor
def delete_author(author_id):
    endpoint = "/Authors/{}".format(str(author_id))
    peticion = requests.delete(url + endpoint)
    return peticion


# Obtener un autor
def get_author(author_id):
    endpoint = "/Authors/{}".format(str(author_id))
    peticion = requests.get(url + endpoint)
    return peticion


# Actualizar un autor
def update_author(author_id, book_id, first_name, last_name):
    endpoint = "/Authors/{}".format(str(author_id))
    headers = {"Content-Type": "application/json"}
    payload = {
        "ID": author_id,
        "IDBook": "{}".format(book_id),
        "FirstName": "{}".format(first_name),
        "LastName": "{}".format(last_name),
    }
    peticion = requests.put(url + endpoint, data=payload, headers=headers)
    return peticion

