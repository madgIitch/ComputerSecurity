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

    with open("txts/cyphertext_1.txt", 'r') as f:
        mess=f.readlines()
        print(encrypt(keys[1],mess[0]))
        f.close()  






#Works!!!!!!

def check2():
    keys = "That chocolate lava cake was divine! Already craving it again. We should definitely explore more dessert places soon."
    secret = "6550524d45050d5f060954501507165e5414571900505f501047554418555b46580f501016750a4b0004074a43521605445d0c06455f1611035f575d0b18446e5019470e5f105e064150575208085840065b4c455d4044090e435c180e5e4353415c00154303431241115d025b061017405f595e48"

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
    encriptado = 
    plano = ""