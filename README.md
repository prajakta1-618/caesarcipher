# caesarcipher
Set of codes to play Caesar Cipher with a set of three friends.

Download all the codes in branch 'codes' on your machine. Watch this https://www.khanacademy.org/computing/computer-science/cryptography/modern-crypt/v/diffie-hellman-key-exchange-part-2 video to understand the Diffie Hellman Key Exchange method of exchanging the key to Caesar cipher. 

You'll need three people to play this simple game, Bob(who will send the message), Alice(to whom the message is directed to) and Eve(who will do the evedropping to get the secret message). All these codes and the 'public keys' mentioned in the codes will be available to all the three people. B and A will decide upon two numbers publically for finding the mod to (watch the video) and the base. The secret numbers of both B and A will be limited to themselves. Bob's secret number is only known to bob and same for Alice. 

First run 'sharingkeys.py' to get the public keys and exchange with each other (Eve can know this keys too) and to get the secret key. This key is shared by B and A, but they need not tell each other its value as this is the main key to decrypting and Eve shouldn't know this at any cost. 

If you're Bob, run 'encryption.py' and type your secret message. Use the secret key you've got to encrypt it. Send the output (encrypted message) to Alice. Let's assume Eve has access to this message too. But she cannot do anything unless she figures out the key. Eve will try to decrypt this message using all the info she has(she, at max, can have two public keys from B and A, the encrypted message, access to all these code as they are publically available).

If you are Alice, you'll receive the encrypted mesaage from Bob. Run 'Decryption.py' and run Bob's message through it using the secret key you had got. Ta-daa! Bob and Alice have successfully shared a code message! But, if Eve, with some technique, is succesful in decrypting evedropped message, the she wins and your info gets stolen :(

All the best! :)
