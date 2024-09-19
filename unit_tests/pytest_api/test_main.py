import uuid
import requests #Importa la librearía de peticiones

ENDPOINT = "https://todo.pixegami.io" #Establece como endpoint la URL
response = requests.get(ENDPOINT) #Guarda la respuesta obteniendo el endpoint

print(response) #Muestra el resultado (200 si es correcto)

#Para obtener toda la información en formato json
data = response.json() #Guarda en formato json los datos
print(data) #Muestra los datos

status_code = response.status_code #Guarda el estado de la respuesta
print(status_code) #Muestra el estado ede la respuesta

#Test para llamar a los endpoint
def test_can_call_endpoint():
    response = requests.get(ENDPOINT) #Almacena la respuesta obteniendo el ENDPOINT
    assert response.status_code == 200 #Assert para probar el estado con código 200

#Test para crear una tarea
def test_can_create_task():

    payload = new_task_payload() #Cargamos el contenido
    create_task_response = create_task(payload) #Indica la tarea que se quiere realizar pasando el contenido generado
    assert create_task_response.status_code == 200 #Como antes, para probar el estado con código 200

    data = create_task_response.json()
    print(data)

    #Obtenemos primero el ID de la tarea
    task_id = data ["task"]["task_id"] #La disposición de los valores depende de como se muestre en la consola al ejecutar los tests
    #Vemos en la consola que primero se nos muestra la tarea y despues su ID, de ahí que se escriba de esta manera
    
    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    assert get_task_data["content"] == payload["content"]
    assert get_task_data["user_id"] == payload["user_id"]
    print(get_task_data)
    
#Test para actualizar un elemento
def test_can_update_task():
    #1.- Crear tarea
    payload = new_task_payload()
    create_task_response = create_task(payload)
    task_id = create_task_response.json()["task"]["task_id"]
    
    #2- Actualizar tarea
    new_payload = {
        "user_id": payload ["user_id"],
        "task_id" : task_id,
        "content": "my updated content",
        "is_done" : True,
    }
    update_task_response= update_task(new_payload)
    assert update_task_response.status_code == 200
    
    #Obtener y validar tarea
    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    assert get_task_data["content"] == new_payload["content"]
    assert get_task_data["is_done"] == new_payload["is_done"]

#Lista las tareas para un usuario
def test_can_list_tasks():
    n = 3 #Numero de tareas que se van a generar
    payload = new_task_payload() #Generación del contenido
    
    for _ in range (n): #Bucle que se recorrera el numero de veces indicado anteriormente para la creación de las tareas
        create_task_response = create_task(payload)
        assert create_task_response.status_code==200 #Assert para comprobar el estado
    
    #Listar tareas
    user_id = payload["user_id"] #Obtiene el ID de usuario de la carga
    list_task_response = list_tasks(user_id) #Guarda la lista de tareas por ID de usuario
    assert list_task_response.status_code==200 #Assert para comprobar el estado
    data = list_task_response.json() #Guarda el json

    tasks = data["tasks"]
    assert len(tasks) == n #Comprueba el numero de tareas
    print(data) #Muestra las tareas

#Eliminar las tareas de un usuario
def test_can_delete_task():
    #Crear tarea
    payload = new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200
    task_id = create_task_response.json()["task"]["task_id"]

    #Borrar la tarea
    delete_task_response = delete_task(task_id)
    assert delete_task_response.status_code == 405 #200 Da error porque el resultado es 405

    #Comprobar que no existe
    get_task_response = get_task(task_id)
    print(get_task_response.status_code)

#Métodos para optimizar
#Cada método llama al endpoint necesario para la función deseada
#Crear tarea
def create_task (payload):
    return requests.put(ENDPOINT + "/create-task", json=payload)

#Actualiza la tarea
def update_task (payload):
    return requests.put(ENDPOINT + "/update-task", json=payload)

#Obtener la tarea
def get_task(task_id):
    return requests.get(ENDPOINT + f"/get-task/{task_id}")

#Lista la tarea
def list_tasks(user_id):
    return requests.get(ENDPOINT + f"/list-tasks/{user_id}")

#Crea el contenido
def new_task_payload():
    #Generamos el id y contenido aleatorios con UUID
    user_id = f"test_user_{uuid.uuid4().hex}"
    content = f"test_content_{uuid.uuid4().hex}"

    #Mensaje de diagnostico con los datos que hemos creado aleatoriamente
    print(f"Creando tarea para el usuario {user_id} con el contenido {content}")

    #Inicializa el contenido
    return { 
        "content": content,
        "user_id": user_id,
        "task_id": "test_task_id",
        "is_done": False
    }

#Elimina la tarea
def delete_task(task_id):
    return requests.get(ENDPOINT + f"/delete-task/{task_id}")