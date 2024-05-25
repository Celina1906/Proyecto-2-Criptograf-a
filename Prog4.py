import os
import pickle
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# Load TGS key
with open('tgs_key.key', 'rb') as f:
    tgs_key = f.read()

# Load message from TGS
with open('message_to_tgs.bin', 'rb') as f:
    encrypted_message = f.read()

# Extract IV and encrypted message
iv = encrypted_message[:16]
encrypted_message = encrypted_message[16:]

# Decrypt message from TGS
cipher = Cipher(algorithms.AES(tgs_key), modes.CFB8(iv))
decryptor = cipher.decryptor()
decrypted_message = decryptor.update(encrypted_message) + decryptor.finalize()

# Deserialize decrypted message using pickle
tgs_message = pickle.loads(decrypted_message)

# Generate SS response
ss_response = f"Response to {tgs_message['service_id']} for {tgs_message['user_id']}"

# Encrypt SS response with TGS key
cipher = Cipher(algorithms.AES(tgs_key), modes.CFB8(iv))
encryptor = cipher.encryptor()
encrypted_ss_response = encryptor.update(ss_response.encode()) + encryptor.finalize()

with open('response_to_client.bin', 'wb') as f:
    f.write(iv + encrypted_ss_response)
