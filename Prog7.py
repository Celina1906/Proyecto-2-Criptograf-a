import json
from Crypto.Cipher import AES

def exec():
    # Leer el mensaje final procesado por el cliente
    with open("message5.bin", "rb") as f:
        nonce, tag, ciphertext = [f.read(x) for x in (16, 16, -1)]

    # Leer el message_to_service.json para obtener la service_key
    with open("message_to_service.json", "r") as f:
        ST = json.load(f)

    service_key = bytes.fromhex(ST["service_key"])

    # Desencriptar el mensaje usando la llave service_key
    cipher = AES.new(service_key, AES.MODE_EAX, nonce=nonce)
    response = json.loads(cipher.decrypt_and_verify(ciphertext, tag).decode())

    # Simulación de la provisión del servicio
    if response["status"] == "success":
        print("Acceso al servicio concedido. Timestamp:", response["timestamp"])
        
        # Aquí puedes definir los servicios disponibles
        services = {
            "serviceABC": "Este mensaje corresponde al servicio con identificador: serviceABC",
            "serviceDEF": "Este mensaje corresponde al servicio con identificador: serviceDEF",
            "serviceXYZ": "Este mensaje corresponde al servicio con identificador: serviceXYZ"
        }
        
        # Proveer el servicio solicitado
        service_id = ST["service_id"]
        if service_id in services:
            print("\nServicio proporcionado:", services[service_id], "\n")
        else:
            print("Error: Servicio no encontrado.")
    else:
        print("Acceso al servicio denegado.")
