import json
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def process_final_message():
    with open("message3.json", "r") as f:
        message3 = json.load(f)
    
    service_session_key = get_service_session_key()  # Implementación de obtener la llave de sesión de servicio

    response_encrypted = bytes.fromhex(message3["response"])
    response_decrypted = decrypt_data(response_encrypted, service_session_key)

    print("Final Message: ", response_decrypted.decode())

def decrypt_data(data, key):
    iv = data[:16]
    ciphertext = data[16:]
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    return decryptor.update(ciphertext) + decryptor.finalize()

def get_service_session_key():
    # Esta función debe implementar la recuperación segura de la llave de sesión de servicio
    return b'service_session_key'  # Esta es solo una simulación

process_final_message()

