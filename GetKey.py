alice = int(input('Enter public key shared by Alice:'))
secretkey = (alice ^ secret) % mod
print(f'The secret key shared by you and Alice is {secretkey}. Do not share this with anyone. Enter this in the cipher "encryption.py" or "Decryption.py"')
