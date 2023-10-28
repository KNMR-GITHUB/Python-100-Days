def encrypt(plain_text,key):
    cipher_text = ""
    for i in range(len(plain_text)):
        if ord(plain_text[i])+key < 122:
            cipher = chr(ord(plain_text[i]) + key)
        else:
            cipher = chr((ord(plain_text[i])+ key)%122 + 96)
        cipher_text+=cipher
    return cipher_text

def decrypt(cipher_text,key):
    P_T = ""
    for i in range(len(cipher_text)):
        if ord(cipher_text[i]) - key > 96:
            plain = chr(ord(cipher_text[i]) - key)
        else:
            plain = chr(122 - (96 - (ord(cipher_text[i]) - key)))
        P_T+=plain
    return P_T

Message = input("Enter the message you wish to pass.\n")

Shift = int(input("Enter the no. of shift you need. \n"))

Operation = input("Enter what you wish to do with the message: 'E' to encrypt or 'D' to decrypt \n")

if Operation == 'E':
    output = encrypt(plain_text = Message, key = Shift)
    print(output)
else:
    output = decrypt(cipher_text = Message, key = Shift)
    print(output)