import requests 

url = "https://fakerestapi.azurewebsites.net/api"


# Obtener todas las actividades
def get_all_activities():
    endpoint = "/activities" 
    peticion = requests.get(url + endpoint) 
    return peticion


# Obtener una actividad
def get_activity(id):
    endpoint = "/activities/{}".format(str(id)) 
    peticion = requests.get(url + endpoint) 
    return peticion


# Crear una actividad
def create_activity(id, activity_name, date, status):

    endpoint = "/activities" 
    headers = {"Content-Type":"application/json"}
    payload = { 
        "ID": id, 
        "Title": "{}".format(activity_name), 
        "DueDate": "".format(date), 
        "Completed": status 
    }
    peticion = requests.post(url + endpoint, data=payload, headers=headers)
    return peticion


# Actualizar/Editar una actividad
def edit_activity(id, activity_name, date, status):
    endpoint = "/activities/{}".format(str(id))
    headers = {"Content-Type": "application/json"}
    payload = { 
        "ID": id, 
        "Title": "{}".format(activity_name), 
        "DueDate": "".format(date), 
        "Completed": status 
    }
    peticion = requests.put(url + endpoint, data=payload, headers=headers)
    return peticion


# Eliminar una actividad
def delete_activity(id): 
    endpoint = "/activities/{}".format(str(id)) 
    peticion = requests.delete(url + endpoint) 
    return peticion
