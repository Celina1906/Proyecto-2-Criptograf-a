import cryptography
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import os

def cargar_llave_privada(filename):
    with open(filename, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None
        )
    return private_key

def construir_mensaje_TGS():
    # Cargar llave privada del TGS
    llave_privada_TGS = cargar_llave_privada("llave_privada_TGS.pem")

    # Aquí se construiría el mensaje para enviar al TGS
    mensaje = "Mensaje para el TGS"
    mensaje_encriptado = llave_privada_TGS.sign(
        mensaje.encode(),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    # Guardar el mensaje en un archivo
    with open("mensaje_para_TGS.txt", "wb") as f:
        f.write(mensaje_encriptado)

if __name__ == "__main__":
    construir_mensaje_TGS()
