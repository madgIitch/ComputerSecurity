#functions
import hashlib
import itertools
import nltk


path = "C:\\Users\\peorr\\OneDrive\\Documentos\\GitHub\\ComputerSecurity\\decrypt"
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
    try: 
        ciphertext_bin = bytes.fromhex(ciphertext)
    except:
        ciphertext_bin=ciphertext



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


####language check
import nltk
nltk.download('words')
from nltk.corpus import words

#compare words
english_words = words.words()
filtered_words = set([word for word in english_words if len(word) > 3])

def has_matching_word(strings_list):  # Convert the English dictionary to a set for faster lookup

    for word in strings_list:
        if word.lower() in filtered_words:  # Convert both strings to lowercase for case-insensitive comparison
            return " ".join(strings_list)
        
    return None

#generate all possible 16 bit
combinations = list(map(convert_int_tuple_to_string, itertools.product([0, 1], repeat=16)))
combinations = list(map(convert_binary_string_to_bytes_and_bytearray,combinations))
#generate keys from possible combinations
keys = list(map(generate_key,combinations))

#######DECYPER MESSAGE ######################

#open message
with open(path+'/Ciphertext-3.txt', 'r') as f:
    secret= f.readlines()
    print(secret)
    f.close()
#decrypt
dec = list(map(lambda x: decrypt(secret[0],x),keys))
dec2 = list(map(lambda x: x.split(" "),dec))
print(dec2)
#see matching words
dec3 = list(map(lambda x: has_matching_word(x),dec2))
print(dec3)
#print possible
dec4= list(filter(lambda x: x != None, dec3))
print(dec4)