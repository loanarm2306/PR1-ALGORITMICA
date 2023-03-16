# Pràctica 1: ENCODING
# Codi font: decoder_rec.py
# Roberta Alina Mititelu -> Y0636484L
# Loana Rodrigues Morais -> O4036247

import sys
import string


# Tractament d'arxius (obertura, lectura i tancament)
def read_text():
    file1 = open(encoded, "r")
    file2 = open(decoded, "r")

    text1 = file1.read()
    text2 = file2.read()

    file1.close()
    file2.close()

    print("\nText codificat: ")
    print(text1)

    print("\nText que s'hauria de trobar al descodificar: ")
    print(text2)

    decoder_rec(text1, text2)


# Descodificar el missatge
def decoder_rec(text1, text2):
    global encoded_text1, letter_cont, key_desp

    decoded_upper = []
    decoded_lower = []
    key_array = []

    decoded_upper = string.ascii_uppercase
    decoded_lower = string.ascii_lowercase

    for k in range(len(key)):
        key_position = string.ascii_lowercase.find(key[k])
        key_array.append(key_position)

    key_length = len(key)
    alphabet_length = len(decoded_lower)

    # Cas base
    if len(text1) == 0:
        return check_text(encoded_text1, text2)
    # Cas recursiu
    else:
        # Cas de la lletra sigui majúscula
        if text1[0].isupper():
            alphabet_position = string.ascii_uppercase.find(text1[0])
            key_desp = letter_cont % key_length
            alphabet_final_position = alphabet_position - key_array[key_desp]
            final_position = alphabet_final_position % alphabet_length
            encoded_text1.append(decoded_upper[final_position])
            letter_cont += 1
        # Cas de la lletra minúscula
        elif text1[0].islower():
            alphabet_position = string.ascii_lowercase.find(text1[0])
            key_desp = letter_cont % key_length
            alphabet_final_position = alphabet_position - key_array[key_desp]
            final_position = alphabet_final_position % alphabet_length
            encoded_text1.append(decoded_lower[final_position])
            letter_cont += 1
        # Cas de la lletra sigui un caràcter especial
        else:
            encoded_text1.append(text1[0])
        
        return decoder_rec(text1[1:], text2)


# Verificar que el text del segon arxiu introduït sigui igual al obtingut després de descodificar
def check_text(decoded_text1, text2):
    decoded_text1 = ''.join(decoded_text1)
    print("\nText descodificat per nosaltres: ")
    print(decoded_text1)

    print("\nComprovació: ")
    if len(decoded_text1) == len(text2):
        if decoded_text1 == text2:
            print("El text1, ha sigut descodificat correctament!")
        else:
            print("Error, el text1 no s'ha descodificat correctament!")


if __name__ == '__main__':
    global encoded_text1, letter_cont, key_desp
    encoded_text1 = []
    letter_cont = 0
    key_desp = 0
    
    # Comprovar que el nombre de paràmetres d'entrada és igual a 4
    # [Nom de l'arxiu] [key] [plain_text.txt] [encoded_text.txt]
    if len(sys.argv) != 4:
        sys.exit('Usage: ' + sys.argv[0] + ' <key>' + ' <encoded_text.txt>' + ' <decoded_text.txt>')
    
    key = sys.argv[1]
    encoded = sys.argv[2]
    decoded = sys.argv[3]
    
    read_text()
