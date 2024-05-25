from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import json

# Generar un par de llaves RSA para el TGS
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

# Guardar la llave privada en un archivo seguro
with open("TGS_private_key.pem", "wb") as f:
    f.write(private_key)

# Supongamos que el AS ya tiene la clave pública del TGS
# Cargar la clave pública del AS (esto sería preestablecido)
with open("AS_public_key.pem", "rb") as f:
    AS_public_key = RSA.import_key(f.read())

# Encriptar la llave privada del TGS usando la clave pública del AS
cipher_rsa = PKCS1_OAEP.new(AS_public_key)
encrypted_private_key = cipher_rsa.encrypt(private_key)

# Guardar la llave privada encriptada en un archivo
with open("encrypted_TGS_private_key.bin", "wb") as f:
    f.write(encrypted_private_key)

print("Llave privada del TGS generada y enviada al AS (encrypted_TGS_private_key.bin)")
