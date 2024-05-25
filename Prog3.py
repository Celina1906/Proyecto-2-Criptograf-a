import os
import pickle
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# Load client key
with open('client_key.key', 'rb') as f:
    client_key = f.read()

# Load message from TGS
with open('message_to_tgs.bin', 'rb') as f:
    encrypted_message = f.read()

# Extract IV and encrypted message
iv = encrypted_message[:16]
encrypted_message = encrypted_message[16:]

# Decrypt message from TGS
cipher = Cipher(algorithms.AES(client_key), modes.CFB8(iv))
decryptor = cipher.decryptor()
decrypted_message = decryptor.update(encrypted_message) + decryptor.finalize()
tgs_message = pickle.loads(decrypted_message)

# Generate SS key
ss_key = os.urandom(32)
with open('ss_key.key', 'wb') as f:
    f.write(ss_key)

# Message to SS
ss_message = {
    'user_id': tgs_message['user_id'],
    'service_id': tgs_message['service_id'],
    'ss_key': ss_key
}

# Encrypt ss_message with TGS key
with open('tgs_key.key', 'rb') as f:
    tgs_key = f.read()

cipher = Cipher(algorithms.AES(tgs_key), modes.CFB8(iv))
encryptor = cipher.encryptor()
encrypted_ss_message = encryptor.update(pickle.dumps(ss_message)) + encryptor.finalize()

with open('message_to_ss.bin', 'wb') as f:
    f.write(iv + encrypted_ss_message)
