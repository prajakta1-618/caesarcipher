def decrypt(text,s):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if (ord(char) >= 65 and ord(char) <= 90):
            result += chr((ord(char) + s-65) % 26 + 65)

        # Encrypt lowercase characters
        elif (ord(char) >= 97 and ord(char) <= 122):
            result += chr((ord(char) + s - 97) % 26 + 97)

        elif (ord(char) >= 48 and ord(char) <= 57):
            result += chr((ord(char) + s - 48) % 10 + 48)

        elif (ord(char) >= 33 and ord(char) <= 47):
            result += chr((ord(char) + s - 32) %15 + 32)

        elif (ord(char) == 32):
            result += chr(32)


    return result

text = input("Enter the text to be encrypted: ")
s = int(input('Enter the secret shared key: '))
decrypted = decrypt(text, -s)
print('The decrypted message is ', decrypted)
