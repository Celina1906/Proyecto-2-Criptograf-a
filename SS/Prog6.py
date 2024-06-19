from Crypto.Cipher import AES
import json

def exec():
    # Leer el mensaje para el Servidor de Servicios para obtener el service_key
    with open("SS/message_to_service.json", "r") as f:
        ST = json.load(f)

    service_key = bytes.fromhex(ST["service_key"])

    # Leer el mensaje 5
    with open("SS/message5.bin", "rb") as f:
        nonce, tag, ciphertext = [f.read(x) for x in (16, 16, -1)]

    # Desencriptar el mensaje usando la llave service_key
    cipher = AES.new(service_key, AES.MODE_EAX, nonce=nonce)
    response = json.loads(cipher.decrypt_and_verify(ciphertext, tag).decode())

    # Procesar el mensaje final
    if response["status"] == "success":
        print("Acceso al servicio concedido. Timestamp:", response["timestamp"])
    else:
        print("Acceso al servicio denegado.")
