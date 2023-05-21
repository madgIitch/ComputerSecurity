import hashlib
import os

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

# Imprimir las claves generadas
for i, key in enumerate(key_list):
    print(f"Clave {i + 1}: {key.hex()}")



#Test
generate_key()