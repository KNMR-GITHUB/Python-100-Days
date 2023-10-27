def encode_decode(text,shift,oper):
    Ntext = list(text)
    if oper == "1":
        for i in range(0,len(text)):
            asciiVal = (ord(text[i]) + shift)
            Ntext[i] = chr(mod(asciiVal))
        print(LtoStr(Ntext))
    elif oper == "2":
        for i in range(0,len(text)):
            asciiVal = (ord(text[i]) - shift)
            Ntext[i] = chr(mod(asciiVal))
        print(LtoStr(Ntext))

def mod(asciiVal):
    if asciiVal < 90 and asciiVal > 64:
        return asciiVal
    elif asciiVal > 90:
        return 65 + (asciiVal % 90) % 26
    elif asciiVal < 65:
        return  91 - (65 - asciiVal)

def LtoStr(l1):
    s1 = ""
    for i in range(0,len(l1)):
        s1 += l1[i]
    return s1


oper = input("What oper would you like to do: \n 1 for Encode \n 2 for Decode \n")
text = input("Enter your message: ")
shift = int(input("Enter the shift: "))
encode_decode(text,shift,oper)




