from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import json
import datetime


def exec(user_id, password):
    # Llave secreta del usuario (previamente compartida)
    user_key = get_random_bytes(16)

    # Guardar user_key en un archivo seguro
    with open("user_key.bin", "wb") as f:
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
    with open("message1.bin", "wb") as f:
        [f.write(x) for x in (cipher.nonce, tag, ciphertext)]

    print("Mensaje 1 generado y almacenado en message1.bin")
