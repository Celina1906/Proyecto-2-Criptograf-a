from Crypto.Cipher import AES
import json

def exec():
    # Cargar la llave secreta del usuario desde el archivo
    with open("user_key.bin", "rb") as f:
        user_key = f.read()

    # Leer el mensaje 1
    with open("message1.bin", "rb") as f:
        nonce, tag, ciphertext = [f.read(x) for x in (16, 16, -1)]

    # Desencriptar el mensaje usando la llave secreta del usuario
    cipher = AES.new(user_key, AES.MODE_EAX, nonce=nonce)
    response = json.loads(cipher.decrypt_and_verify(ciphertext, tag).decode())

    # Construir mensaje para el TGS
    TGT = response["TGT"]

    # Guardar el TGT en un archivo
    with open("message_to_TGS.json", "w") as f:
        json.dump(TGT, f)

    print("Mensaje para el TGS generado y almacenado en message_to_TGS.json")
