import hashlib
import os
import random
import platform

def run():

    # Variable que contiene las rutas base
    ruta_1 = "/Users/felixbarenysmarimon/Desktop/UNIVERISTAT/ERASMUS FU/Computer Security/assigments/txts/"
    ruta_2 = "C:\\Users\\peorr\\OneDrive\\Documentos\\GitHub\\ComputerSecurity\\txts\\"

    # Variable que contiene la ruta seleccionada
    ruta = ruta_1 if platform.system() == "Darwin" else ruta_2

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

    # Guardar las claves en un archivo .txt
    with open(ruta + "keys.txt", 'w') as f:
        for i in range(len(key_list)):
            f.write(key_list[i].hex())
            f.write('\n')

    ### One time pad ENCRYPTION 

    def encrypt(key, secret):
        crypted = ''.join([chr(ord(c) ^ ord(secret[i])) for i, c in enumerate(key[:len(secret)])])
        return crypted

    #######################

    # Encrypt seven PT messages (say m1, ..., m7) using OTP, each with a unique key (say k1,...,k7).
    for i in range(7):
        # Encrypt message
        with open(ruta + "plaintext_" + str(i) + ".txt") as f:
            secret = f.readlines()
            message_encr = encrypt(key=key_list[i].hex(), secret=secret[0])

        # Save it
        with open(ruta + "cyphertext_" + str(i) + ".txt", 'w') as f:
            f.write(message_encr)

    #######################

    # Pick any three messages from the above set {m1, ..., m7} and re-encrypt again, each time with a new unique key (k8, k9, k10).

    # Choose randomly 3 numbers
    random_mess = random.sample(range(7), 3)
    keys = [7, 8, 9]

    for i, x in enumerate(random_mess):
        with open(ruta + "cyphertext_" + str(x) + ".txt", 'r') as f:
            secret = f.readlines()
            mess_encrypt = encrypt(key_list[keys[i]].hex(), secret[0])

        # Save it
        with open(ruta + "cyphertext2_" + str(x) + "_" + str(keys[i]) + ".txt", 'w') as f:
            f.write(mess_encrypt)

    ###################

    # For the remaining three messages m8, m9, m10 encrypt while re-using one key from the set {k1, ..., k7} for each message.

    messages = [7, 8, 9]
    random_keys = random.sample(range(7), 3)

    for i, x in enumerate(random_keys):
        with open(ruta + "plaintext_" + str(messages[i]) + ".txt", 'r') as f:
            secret = f.readlines()
            mess_encrypt = encrypt(key_list[x].hex(), secret[0])

        # Save it
        with open(ruta + "cyphertext_" + str(messages[i]) + "_" + str(x) + ".txt", 'w') as f:
            f.write(mess_encrypt)


####TESTING

run()