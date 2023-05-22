import hashlib
import os
import random

########### GENERATE KEYS ###############################
def generate_key():
    # Generar una clave de 16 bits aleatoria
    k0 = bytearray(os.urandom(2))

    # Cálculo de k1 como un desplazamiento cíclico de 1 bit a la derecha de k0
    k1 = bytearray([(k0[0] >> 1) | ((k0[1] & 0x01) << 7), (k0[1] >> 1)])

    # Cálculo de los hashes SHA-512 de k0 y k1
    h0 = hashlib.sha512(k0).digest()
    h1 = hashlib.sha512(k1).digest()

    # Concatenar h0 y h1 para formar la clave de 1024 bits (128 bytes)
    key = h0 + h1

    return key

# Generar una lista de claves
key_list = [generate_key() for _ in range(10)]  # Cambiar 10 por el número deseado de claves
#Guardar llaves en fichero .txt


with open("/Users/felixbarenysmarimon/Desktop/UNIVERISTAT/ERASMUS FU/Computer Security/assigments/txts/keys.txt", 'w') as f:
    for i in range(len(key_list)):
        f.write(key_list[i].hex())
        f.write('\n')
    f.close()  

    



### One time pad ENCRYPTION 

def encrypt(key, secret):
    crypted = ''.join(
        [chr(ord(c) ^ ord(secret[i])) for i, c in enumerate(key[:len(secret)])])
    return crypted

#######################
#Encrypt seven PT messages (say m1 , . . . , m7 ) using OTP, each with a unique key (say k1,...,k7).

for i in range(7):
    #encrypt message
    with open("/Users/felixbarenysmarimon/Desktop/UNIVERISTAT/ERASMUS FU/Computer Security/assigments/txts/plaintext_"+str(i)+".txt") as f:
        secret = f.readlines()
        message_encr = encrypt(key=key_list[i].hex(),secret=secret[0])
        f.close()
    #save it

    with open("/Users/felixbarenysmarimon/Desktop/UNIVERISTAT/ERASMUS FU/Computer Security/assigments/txts/cyphertext_"+str(i)+".txt", 'w') as f:
        f.write(message_encr)
        f.close()

#######################
#Pick any three messages from the above set {m1, . . . , m7} and re-encrypt again, each time
#with a new unique key (k8, k9, k10).

 #choose randomly 3 numbers
random_mess = random.sample(range(7),3)
keys = [7,8,9]
#open
for i,x in enumerate(random_mess):
    
    with open("/Users/felixbarenysmarimon/Desktop/UNIVERISTAT/ERASMUS FU/Computer Security/assigments/txts/cyphertext_"+str(x)+".txt", 'r') as f:
        secret= f.readlines()
        mess_encrypt = encrypt(key_list[keys[i]].hex(),secret[0])
        f.close()
     #save it

    with open("/Users/felixbarenysmarimon/Desktop/UNIVERISTAT/ERASMUS FU/Computer Security/assigments/txts/cyphertext2_"+str(x)+"_"+str(keys[i])+".txt", 'w') as f:
        f.write(mess_encrypt)
        f.close()
##################
#For the remaining three messages m8,m9,m10 encrypt while re-using one key from the set {k1, . . . , k7} for each message.
    
        
messages = [7,8,9]
random_keys = random.sample(range(7),3)

#open
for i,x in enumerate(random_keys):
    
    with open("/Users/felixbarenysmarimon/Desktop/UNIVERISTAT/ERASMUS FU/Computer Security/assigments/txts/plaintext_"+str(messages[i])+".txt", 'r') as f:
        secret= f.readlines()
        mess_encrypt = encrypt(key_list[x].hex(),secret[0])
        f.close()
     #save it

    with open("/Users/felixbarenysmarimon/Desktop/UNIVERISTAT/ERASMUS FU/Computer Security/assigments/txts/cyphertext_"+str(messages[i])+"_"+str(x)+".txt", 'w') as f:
        f.write(mess_encrypt)
        f.close()








    

