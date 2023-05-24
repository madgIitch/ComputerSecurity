import hashlib
import os
import random
import platform


# Variable que contiene las rutas base
ruta_1 = "/Users/felixbarenysmarimon/Desktop/UNIVERISTAT/ERASMUS FU/Computer Security/assigments/txts/"
ruta_2 = "C:\\Users\\peorr\\OneDrive\\Documentos\\GitHub\\ComputerSecurity\\pruebaPepe\\"

# Variable que contiene la ruta seleccionada
ruta = ruta_1 if platform.system() == "Darwin" else ruta_2
    

def run_encryption():
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


    key_list = [generate_key() for _ in range(10)]

    with open(ruta + "keys.txt", 'w') as f:
        for i in range(len(key_list)):
            f.write(key_list[i].hex())
            f.write('\n')

    def encrypt(key, secret):
        crypted = ''.join([chr(ord(c) ^ ord(secret[i])) for i, c in enumerate(key[:len(secret)])])
        return crypted

    for i in range(7):
        with open(ruta + "plaintext_" + str(i) + ".txt") as f:
            secret = f.readlines()
            message_encr = encrypt(key=key_list[i].hex(), secret=secret[0])

        with open(ruta + "cyphertext_" + str(i) + ".txt", 'w') as f:
            f.write(message_encr)

        

        # Run decryption after each encryption


def decrypt(key, ciphertext):
    key_bytes = bytes.fromhex(key)  # Convertir la clave hexadecimal a bytes
    key_str = key_bytes.decode('latin1')  # Convertir la clave de bytes a cadena de caracteres
    decrypted = ''.join([chr(c ^ key_bytes[i % len(key_bytes)]) for i, c in enumerate(ciphertext.encode('latin1'))])
    return decrypted

def run_decryption():
    ruta_keys = ruta + "keys.txt"

    with open(ruta_keys, 'r') as f:
        key_lines = f.readlines()

    keys = [line.strip() for line in key_lines]

    for i in range(7):
        with open(ruta + "cyphertext_" + str(i) + ".txt", 'r') as f:
            ciphertext = f.read().strip()

        # Obtener la clave utilizada en esta iteración
        if i < 7:
            key_index = i
        elif i < 10:
            key_index = i - 7
        else:
            key_index = i % 7

        key_used = keys[key_index]

        decrypted_message = decrypt(key_used, ciphertext)

        print("Decrypted message", i+1, ":", decrypted_message)


# Ejecutar encriptación y desencriptación
run_encryption()

run_decryption()
