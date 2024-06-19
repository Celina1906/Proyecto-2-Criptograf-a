from Crypto.Cipher import AES
import json

# Definición de service_id

def exec():
    # Leer el mensaje 3
    with open("TGS/message3.bin", "rb") as f:
        nonce, tag, ciphertext = [f.read(x) for x in (16, 16, -1)]

    # Cargar el TGT_key desde el archivo `message_to_TGS.json` (porque fue usado para encriptar el mensaje)
    with open("TGS/message_to_TGS.json", "r") as f:
        TGT = json.load(f)

    TGT_key = bytes.fromhex(TGT["TGT_key"])

    # Desencriptar el mensaje usando la llave TGT_key
    cipher = AES.new(TGT_key, AES.MODE_EAX, nonce=nonce)
    response = json.loads(cipher.decrypt_and_verify(ciphertext, tag).decode())

    # Construir mensaje para el Servidor de Servicios
    ST = response["ST"]

    # Guardar el ST en un archivo
    with open("SS/message_to_service.json", "w") as f:
        json.dump(ST, f)

    print("Mensaje para el Servidor de Servicios generado y almacenado en message_to_service.json")
