from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
import base64

# Cargar la clave privada del AS
with open("AS_private_key.pem", "rb") as f:
    AS_private_key = RSA.import_key(f.read())

# Cargar la clave simétrica cifrada
with open("encrypted_aes_key.bin", "rb") as f:
    encrypted_aes_key = f.read()

# Desencriptar la clave simétrica usando la clave privada del AS
cipher_rsa = PKCS1_OAEP.new(AS_private_key)
aes_key = cipher_rsa.decrypt(encrypted_aes_key)

# Cargar la clave privada cifrada del TGS
with open("encrypted_TGS_private_key.bin", "rb") as f:
    nonce, tag, ciphertext = [f.read(x) for x in (16, 16, -1)]

# Desencriptar la clave privada del TGS usando la clave simétrica (AES)
cipher_aes = AES.new(aes_key, AES.MODE_EAX, nonce=nonce)
private_key = cipher_aes.decrypt_and_verify(ciphertext, tag)

# Guardar la clave privada del TGS desencriptada
with open("TGS_private_key_decrypted.pem", "wb") as f:
    f.write(private_key)

print("Llave privada del TGS desencriptada y guardada en TGS_private_key_decrypted.pem")
