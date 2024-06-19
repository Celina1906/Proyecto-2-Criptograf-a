from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Random import get_random_bytes

def exec():
    # Generar un par de llaves RSA para el TGS
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()

    # Guardar la llave privada en un archivo seguro
    with open("TGS/TGS_private_key.pem", "wb") as f:
        f.write(private_key)

    # Cargar la clave pública del AS (esto sería preestablecido)
    with open("TGS/AS_public_key.pem", "rb") as f:
        AS_public_key = RSA.import_key(f.read())

    # Generar una clave simétrica (AES)
    aes_key = get_random_bytes(32)

    # Encriptar la clave simétrica usando la clave pública del AS
    cipher_rsa = PKCS1_OAEP.new(AS_public_key)
    encrypted_aes_key = cipher_rsa.encrypt(aes_key)

    # Encriptar la clave privada del TGS usando la clave simétrica (AES)
    cipher_aes = AES.new(aes_key, AES.MODE_EAX)
    nonce = cipher_aes.nonce
    ciphertext, tag = cipher_aes.encrypt_and_digest(private_key)

    # Guardar la clave simétrica encriptada y la clave privada encriptada
    with open("AS/encrypted_TGS_private_key.bin", "wb") as f:
        f.write(nonce + tag + ciphertext)

    with open("AS/encrypted_aes_key.bin", "wb") as f:
        f.write(encrypted_aes_key)

    print("Llave privada del TGS generada y enviada al AS (encrypted_TGS_private_key.bin y encrypted_aes_key.bin)")
