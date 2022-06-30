import base64

def encode(txt, key):
    # Verificar taamaño de la clave
    if(len(txt)>len(key)):
        for i in range(len(txt)-len(key)):
            key += key[i]
    elif(len(txt)<len(key)):
        key = key[0:len(txt)]
    # Transformar ascii a binario
    binario = int.from_bytes(txt.encode(), 'big')
    binario2 = int.from_bytes(key.encode(), 'big')
    binario3 = bin(binario ^ binario2)
    # Transformar binario a ascii
    n = int(binario3, 2)
    ascii = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
    # byte shift hacia la izquierda
    ascii = byteShift(ascii,int(len(key)/2),True)
    # Transformar base ascii a base64
    message_bytes = ascii.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')

    print("El texto cifrado es: "+base64_message)
    return base64_message

def decode(txt, key):
    # Transformar base64 a ascii
    base64_message = txt
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    txt = message_bytes.decode('ascii')
    #Verificar taamaño de la clave
    if(len(txt)>len(key)):
        for i in range(len(txt)-len(key)):
            key += key[i]
    elif(len(txt)<len(key)):
        key = key[0:len(txt)]
    # byte shift hacia la derecha
    txt = byteShift(txt,int(len(key)/2),False)
    # Transformar ascii a binario
    binario = int.from_bytes(txt.encode(), 'big')
    binario2 = int.from_bytes(key.encode(), 'big')
    binario3 = bin(binario ^ binario2)
    # Transformar binario a ascii
    n = int(binario3, 2)
    ascii = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()

    print("El texto desifrado es: "+ascii)
    return ascii

def byteShift(input,n,d):
    if d:
        Lfirst = input[0 : n]
        Lsecond = input[n :]
        return Lsecond + Lfirst
    else:
        Rsecond = input[len(input)-n : ]
        Rfirst = input[0 : len(input)-n]
        return Rsecond + Rfirst

def main():
    txt = input("Ingrese el texto a cifrar: ")
    key = input("Ingrese la clave: ")
    if(key[0] != txt[0]):
        encodeString = encode(txt, key)
        decode(encodeString, key)
    else:
        print("El texto no puede ser cifrado con una clave que comienze con el mismo caracter. Genera incosistencias en el cifrado y descifrado.")
main()
    