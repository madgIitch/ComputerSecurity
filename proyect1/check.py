#import keys
def check():
    keys=[]
    with open("txts/keys.txt", 'r') as f:
        keys=f.readlines()
        f.close()  

    def encrypt(key, secret):
        crypted = ''.join(
            [chr(ord(c) ^ ord(secret[i])) for i, c in enumerate(key[:len(secret)])])
        return crypted
    #decrypt one

    with open("txts/cyphertext2_5_7.txt", 'r') as f:
        mess=f.readlines()
        for k in keys:
            print(encrypt(k,mess[0]))
        f.close()  






#Works!!!!!!

def check2():
    keys = "Perfect! See you soon, MJ. Have an amazing day! Can't wait for our picnic. It's going to be wonderful. See you soon!"
    secret = "695c475f545a4419416404551048571011170d580f1414792f1d167100120645075d125854574d0a0c5e18505949154527075717411941020a4d445e5e4a1357444419465b050c51064c4271151643455e5c0b575619405c12035644150e5707531407445f4c12615d04424a094212460a5a5f40"

    def encrypt(key, secret):
        crypted = ''.join([chr(ord(c) ^ ord(secret[i])) for i, c in enumerate(key[:len(secret)])])
        return crypted

    encrypted_text = encrypt(keys, secret)
    with open('llave.txt', 'a') as file:
        file.write(encrypted_text + '\n')

    print(encrypted_text)
    return encrypted_text


def check3():
    keys= check2()
    secret = "6550524d45050d5f060954501507165e5414571900505f501047554418555b46580f501016750a4b0004074a43521605445d0c06455f1611035f575d0b18446e5019470e5f105e064150575208085840065b4c455d4044090e435c180e5e4353415c00154303431241115d025b061017405f595e48"

    def decrypt(key, secret):
        crypted = ''.join(
            [chr(ord(c) ^ ord(secret[i])) for i, c in enumerate(key[:len(secret)])])
        return crypted
    
    
    
    print(decrypt(keys,secret))
        



def check4():
    descifrado = []
    with open('cifradoRestante.txt', 'r') as file:
        cifrado = file.readlines()
    cifrado = [entry.strip() for entry in cifrado]


    def decrypt(key, secret):
        crypted = ''.join(
            [chr(ord(c) ^ ord(secret[i])) for i, c in enumerate(key[:len(secret)])])
        return crypted

    for cif in cifrado:
        descifrado.append(decrypt(cif, check2()))

    print(descifrado)
    return descifrado






