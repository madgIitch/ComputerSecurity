#import keys
keys=[]
with open("txts/keys.txt", 'r') as f:
    keys=f.readlines()
    f.close()  

def encrypt(key, secret):
    crypted = ''.join(
        [chr(ord(c) ^ ord(secret[i])) for i, c in enumerate(key[:len(secret)])])
    return crypted
#decrypt one

with open("txts/cyphertext_0.txt", 'r') as f:
    mess=f.readlines()
    print(encrypt(keys[0],mess[0]))
    f.close()  

#Works!!!!!!