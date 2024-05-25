from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Random import get_random_bytes

# Generar un par de llaves RSA para el Servidor de Servicios
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

# Guardar la llave privada en un archivo seguro
with open("service_private_key.pem", "wb") as f:
    f.write(private_key)

# Cargar la clave pública del TGS (esto sería preestablecido)
with open("TGS_public_key.pem", "rb") as f:
    TGS_public_key = RSA.import_key(f.read())

# Generar una clave simétrica (AES)
aes_key = get_random_bytes(32)

# Cifrar la clave simétrica usando la clave pública del TGS
cipher_rsa = PKCS1_OAEP.new(TGS_public_key)
encrypted_aes_key = cipher_rsa.encrypt(aes_key)

# Cifrar la clave privada del Servidor de Servicios usando la clave simétrica (AES)
cipher_aes = AES.new(aes_key, AES.MODE_EAX)
nonce = cipher_aes.nonce
ciphertext, tag = cipher_aes.encrypt_and_digest(private_key)

# Guardar la clave simétrica cifrada y la clave privada cifrada
with open("encrypted_service_private_key.bin", "wb") as f:
    f.write(nonce + tag + ciphertext)

with open("encrypted_aes_key_for_service.bin", "wb") as f:
    f.write(encrypted_aes_key)

print("Llave privada del Servidor de Servicios generada y enviada al TGS (encrypted_service_private_key.bin y encrypted_aes_key_for_service.bin)")
