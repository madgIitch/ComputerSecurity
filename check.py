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

with open("txts/cyphertext_1.txt", 'r') as f:
    mess=f.readlines()
    print(encrypt(keys[1],mess[0]))
    f.close()  






#Works!!!!!!

llave = []
mensaje = '065c070c51515051035355500055015f5350010709510502090107520256020a52000601510507020c53030c5053515100040404030357510153015002560304520452070356530356575504025a060a010a5009565d06520c070250040602560709040a575f0706520100535008005b05080c52010f540d07090c0751045751555700520402070506565407540f570103060852510553040553050700040c000102000a5106530f57000401050505530450055504575306575705530806060003500204005207030c0a07530653510e51530c53065952570404090a57580c55030107030751030453565651050f05540459'

def desencripta (llave, mensaje):
    desencriptado = ''.join(
        [chr(ord(c) ^ ord(mensaje[i])) for i, c in enumerate(llave[:len(mensaje)])])
    return desencriptado

desencripta(llave, mensaje)