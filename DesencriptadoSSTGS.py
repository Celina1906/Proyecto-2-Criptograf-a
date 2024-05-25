# decrypt_service_key.py
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
import base64

# Cargar la clave privada del TGS
with open("TGS_private_key_decrypted.pem", "rb") as f:
    TGS_private_key = RSA.import_key(f.read())

# Cargar la clave simétrica cifrada
with open("encrypted_aes_key_for_service.bin", "rb") as f:
    encrypted_aes_key = f.read()

# Desencriptar la clave simétrica usando la clave privada del TGS
cipher_rsa = PKCS1_OAEP.new(TGS_private_key)
aes_key = cipher_rsa.decrypt(encrypted_aes_key)

# Cargar la clave privada cifrada del Servidor de Servicios
with open("encrypted_service_private_key.bin", "rb") as f:
    nonce, tag, ciphertext = [f.read(x) for x in (16, 16, -1)]

# Desencriptar la clave privada del Servidor de Servicios usando la clave simétrica (AES)
cipher_aes = AES.new(aes_key, AES.MODE_EAX, nonce=nonce)
private_key = cipher_aes.decrypt_and_verify(ciphertext, tag)

# Guardar la clave privada del Servidor de Servicios desencriptada
with open("service_private_key_decrypted.pem", "wb") as f:
    f.write(private_key)

print("Llave privada del Servidor de Servicios desencriptada y guardada en service_private_key_decrypted.pem")
