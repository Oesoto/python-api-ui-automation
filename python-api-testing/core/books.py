import requests
url = "https://fakerestapi.azurewebsites.net/api"


# Consultar listado de libros
def get_all_books():
    endpoint = "/Books"
    peticion = requests.get(url + endpoint)
    return peticion


# Crear un libro
def create_book(book_id, book_title, description, page_count, excerpt, publish_date):
    endpoint = "/Books"
    headers = {"Content-Type": "application/json"}
    payload = {
        "ID": book_id,
        "Title": "{}".format(book_title),
        "Description": "{}".format(description),
        "PageCount": page_count,
        "Excerpt": "{}".format(excerpt),
        "PublishDate": "".format(publish_date)
    }
    peticion = requests.post(url + endpoint, data=payload, headers=headers)
    return peticion


# Eliminar un libro
def delete_book(book_id):
    endpoint = "/Books/{}".format(str(book_id))
    peticion = requests.delete(url + endpoint)
    return peticion


# Obtener un libro
def get_book(book_id):
    endpoint = "/Books/{}".format(str(book_id))
    peticion = requests.get(url + endpoint)
    return peticion


# Actualizar un libro
def update_book(book_id, book_title, description, page_count, excerpt, publish_date):
    endpoint = "/Books/{}".format(str(book_id))
    headers = {"Content-Type": "application/json"}
    payload = {
        "ID": book_id,
        "Title": "{}".format(book_title),
        "Description": "{}".format(description),
        "PageCount": page_count,
        "Excerpt": "{}".format(excerpt),
        "PublishDate": "".format(publish_date)
    }
    peticion = requests.put(url + endpoint, data=payload, headers=headers)
    return peticion
