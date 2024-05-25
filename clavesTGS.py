from Crypto.PublicKey import RSA

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