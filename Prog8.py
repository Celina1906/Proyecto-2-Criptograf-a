from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

def generate_rsa_keypair_tgs():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()

    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    with open("tgs_private_key.pem", "wb") as f:
        f.write(private_pem)
    with open("tgs_public_key.pem", "wb") as f:
        f.write(public_pem)

def send_private_key_to_as():
    # Simulación del envío de la llave privada usando la llave pública del AS
    with open("tgs_private_key.pem", "rb") as f:
        private_key_data = f.read()

    with open("as_public_key.pem", "rb") as f:
        as_public_key_pem = f.read()

    as_public_key = serialization.load_pem_public_key(as_public_key_pem, backend=default_backend())

    encrypted_private_key = as_public_key.encrypt(
        private_key_data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    with open("encrypted_tgs_private_key_to_as.bin", "wb") as f:
        f.write(encrypted_private_key)

generate_rsa_keypair_tgs()
send_private_key_to_as()
