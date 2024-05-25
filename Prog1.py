from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.kdf.hkdf import HKDFExpand
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
import json

def authenticate_user(user_id, password):
    # Suponemos que el AS ya tiene almacenada la contraseña hash del usuario
    stored_password_hash = b"stored_password_hash"  # Este valor debería venir de una base de datos segura
    
    # Derivar llave de la contraseña ingresada por el usuario
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())
    
    if key != stored_password_hash:
        raise ValueError("Authentication failed")

    # Simula la generación de los mensajes
    session_key = os.urandom(32)
    ticket = {
        "user_id": user_id,
        "session_key": session_key.hex()
    }

    ticket_encrypted = encrypt_data(json.dumps(ticket).encode(), key)

    message1 = {
        "session_key": session_key.hex(),
        "ticket": ticket_encrypted.hex()
    }

    # Guardar los mensajes en archivos
    with open("message1.json", "w") as f:
        json.dump(message1, f)

def encrypt_data(data, key):
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(data) + encryptor.finalize()
    return iv + ciphertext

# Simulación de la autenticación del usuario
authenticate_user("user123", "password123")
