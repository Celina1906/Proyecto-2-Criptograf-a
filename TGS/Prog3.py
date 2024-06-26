import json
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import datetime

def exec(user_id, password, service_id):
    # Leer el mensaje para el TGS
    with open("TGS/message_to_TGS.json", "r") as f:
        TGT = json.load(f)

    # Validar el TGT y generar mensajes para el cliente
    if TGT["user_id"] == user_id and TGT["password"] == password:
        service_key = get_random_bytes(16)
        timestamp = str(datetime.datetime.now())

        # Mensaje 3: Service Ticket (ST)
        ST = {
            "service_id": service_id,
            "service_key": service_key.hex(),
            "timestamp": timestamp
        }

        # Mensaje 4: Respuesta para el cliente
        response = {
            "ST": ST,
            "service_key": service_key.hex()
        }

        # Encriptar mensajes con la llave TGT_key
        TGT_key = bytes.fromhex(TGT["TGT_key"])
        cipher = AES.new(TGT_key, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(json.dumps(response).encode())

        # Guardar mensajes en archivos
        with open("TGS/message3.bin", "wb") as f:
            [f.write(x) for x in (cipher.nonce, tag, ciphertext)]

        print("Mensajes generados y almacenados en message3.bin")
    else:
        print("Error: user_id no coincide.")
