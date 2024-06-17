from Crypto.PublicKey import RSA

def generateAS():
    # Generar un par de llaves RSA para el AS
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()

    # Guardar la llave privada en un archivo seguro
    with open("AS_private_key.pem", "wb") as f:
        f.write(private_key)

    # Guardar la llave pública en un archivo
    with open("AS_public_key.pem", "wb") as f:
        f.write(public_key)

    print("Llaves del AS generadas. Clave pública guardada en AS_public_key.pem")
    
def generateTGS():
    # Generar un par de llaves RSA para el TGS
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()

    # Guardar la llave privada en un archivo seguro
    with open("TGS_private_key.pem", "wb") as f:
        f.write(private_key)

    # Guardar la clave pública en un archivo
    with open("TGS_public_key.pem", "wb") as f:
        f.write(public_key)

    print("Llaves del TGS generadas. Clave pública guardada en TGS_public_key.pem")