from Crypto.PublicKey import RSA

def generate_rsa_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

# Generar claves RSA para AS y TGS
private_key_AS, public_key_AS = generate_rsa_keys()
private_key_TGS, public_key_TGS = generate_rsa_keys()

# Guardar las claves en archivos
with open("private_key_AS.pem", "wb") as f:
    f.write(private_key_AS)
with open("public_key_AS.pem", "wb") as f:
    f.write(public_key_AS)

with open("private_key_TGS.pem", "wb") as f:
    f.write(private_key_TGS)
with open("public_key_TGS.pem", "wb") as f:
    f.write(public_key_TGS)
