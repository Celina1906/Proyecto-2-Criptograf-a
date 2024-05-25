import json
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

def dialog_with_service():
    with open("message_for_service.json", "r") as f:
        message_for_service = json.load(f)
    
    service_session_key = bytes.fromhex(message_for_service["service_session_key"])
    service_ticket = bytes.fromhex(message_for_service["service_ticket"])

    # Servidor de Servicios verifica el ticket y genera un mensaje
    response_message = {
        "status": "success",
        "data": "Here is your service!"
    }

    response_encrypted = encrypt_data(json.dumps(response_message).encode(), service_session_key)

    message3 = {
        "response": response_encrypted.hex()
    }

    with open("message3.json", "w") as f:
        json.dump(message3, f)

def encrypt_data(data, key):
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(data) + encryptor.finalize()
    return iv + ciphertext

dialog_with_service()

