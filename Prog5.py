from Crypto.Cipher import AES
import json
import datetime

def exec(service_id):
    # Leer el mensaje para el Servidor de Servicios
    with open("message_to_service.json", "r") as f:
        ST = json.load(f)

    # Validar el ST y generar respuesta para el cliente
    if ST["service_id"] == service_id:
        timestamp = str(datetime.datetime.now())

        # Mensaje 5: Respuesta del Servidor de Servicios
        response = {
            "status": "success",
            "timestamp": timestamp
        }

        # Encriptar mensajes con la llave service_key
        service_key = bytes.fromhex(ST["service_key"])
        cipher = AES.new(service_key, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(json.dumps(response).encode())

        # Guardar mensaje en archivo
        with open("message5.bin", "wb") as f:
            [f.write(x) for x in (cipher.nonce, tag, ciphertext)]

        print("Respuesta del Servidor de Servicios generada y almacenada en message5.bin")
    else:
        print("Error: service_id no coincide.")
