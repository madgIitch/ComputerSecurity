#functions
import hashlib
import itertools

path = "/Users/felixbarenysmarimon/Desktop/UNIVERISTAT/ERASMUS FU/Computer Security/06"
########### GENERATE KEYS ###############################
def generate_key(k0):
    # Cálculo de k1 como un desplazamiento cíclico de 1 bit a la derecha de k0
    k1 = bytearray([(k0[0] >> 1) | ((k0[1] & 0x01) << 7), (k0[1] >> 1)])

    # Cálculo de los hashes SHA-512 de k0 y k1
    h0 = hashlib.sha512(k0).digest()
    h1 = hashlib.sha512(k1).digest()

    # Concatenar h0 y h1 para formar la clave de 1024 bits (128 bytes)
    key = h0 + h1
    return key.hex()

### One time pad ENCRYPTION 

def decrypt(ciphertext, key):
    # Convert ciphertext and key to binary using hex decoding
    ciphertext_bin = bytes.fromhex(ciphertext)
    key_bin = key.encode('ascii')

    # Compute the plaintext by XORing the ciphertext and key
    plaintext = ''.join(chr(ct_byte ^ key_byte)
                        for ct_byte, key_byte in zip(ciphertext_bin, key_bin))

    return plaintext



def convert_int_tuple_to_string(int_tuple):
    str_list = [str(num) for num in int_tuple]
    string = ''.join(str_list)
    return string

#convert to bytes
def convert_binary_string_to_bytes_and_bytearray(binary_string):
    # Convert binary string to bytes
    byte_data = bytes(int(binary_string[i:i+8], 2) for i in range(0, len(binary_string), 8))
    
    # Convert bytes to bytearray
    byte_data = bytearray(byte_data)
    
    return byte_data


#########################LANGUAGE PROBABILITIES#########################
#function that only returns the sentences with prob >=0.5 to be english language
from langdetect import detect_langs

def is_english(sentence, threshold=0.5):
    try:
        languages = detect_langs(sentence)
        for lang in languages:
            if lang.lang == 'en' and lang.prob >= threshold:
                return sentence
        return ""
    except:
        return ""
    


#generate all possible 16 bit
combinations = list(map(convert_int_tuple_to_string, itertools.product([0, 1], repeat=16)))
combinations = list(map(convert_binary_string_to_bytes_and_bytearray,combinations))


#generate keys from combinations
keys = list(map(generate_key,combinations))


#open message
with open(path+'/Ciphertext-13.txt', 'r') as f:
    secret= f.readlines()
    f.close()
    #save it

print(secret)


#generate decryption of message

dec = list(map(lambda x: decrypt(secret[0],x),keys))
# check probbaility of language english

check =list(map(is_english,dec))
#remove non probable
check[:]= (value for value in check if value != "")
#double language check

check2 =list(map(lambda x: is_english(sentence = x,threshold=0.9999),check))
check2[:]= (value for value in check2 if value != "")



# get key from encryption
keys[560]