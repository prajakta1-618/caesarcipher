mod = int(input('Enter the publicly decided prime modulus: '))
base = int(input('Enter the publically decided generator: '))
secret = int(input('Enter the secret number Bob chose as the index:'))

bob = (base ** secret) % mod

print('Your publicaly sharable key is:', bob)
print('Share this with Alice.')

que = input(' Do you have public key from Alice?(y/n)')
if que == 'y':
    alice = int(input('Enter public key shared by Alice:'))
    secretkey = (alice ** secret) % mod
    print(f'The secret key shared by you and Alice is {secretkey}. Do not share this with anyone.')

elif que == 'n':
    exit
