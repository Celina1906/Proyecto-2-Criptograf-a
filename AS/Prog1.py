from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import json
import datetime

def cargar_usuarios():
    with open('AS/usuarios.json', 'r') as file:
        usuarios = json.load(file)
    return usuarios

def exec(user_id, password):
    # Cargar usuarios desde el archivo JSON
    usuarios = cargar_usuarios()

    # Verificar si el usuario existe
    usuario = None
    for user in usuarios:
        if user["user_id"] == user_id and user["contrasena"] == password:
            usuario = user
            break
    
    if usuario is None:
        print(f"El usuario con ID {user_id} no existe, favor ingresar un usuario válido")
        return -1
    
    # Llave secreta del usuario (previamente compartida)
    user_key = get_random_bytes(16)

    # Guardar user_key en un archivo seguro
    with open("AS/user_key.bin", "wb") as f:
        f.write(user_key)

    # Mensajes que envía el AS al cliente
    TGT_key = get_random_bytes(16)
    timestamp = str(datetime.datetime.now())

    # Mensaje 1: Ticket Granting Ticket (TGT)
    TGT = {
        "user_id": user_id,
        "password": password,
        "TGT_key": TGT_key.hex(),
        "timestamp": timestamp
    }

    # Mensaje 2: Respuesta para el cliente
    response = {
        "TGT": TGT,
        "TGT_key": TGT_key.hex()
    }

    # Encriptar mensajes con la llave secreta del usuario
    cipher = AES.new(user_key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(json.dumps(response).encode())

    # Guardar mensajes en archivos
    with open("AS/message1.bin", "wb") as f:
        [f.write(x) for x in (cipher.nonce, tag, ciphertext)]

    print("Mensaje 1 generado y almacenado en message1.bin")
