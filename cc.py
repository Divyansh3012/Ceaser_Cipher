letters = 'abcdefghijklmonpqrstuvwxyz'
num_leters = len(letters)

def encrypt_decrypt(text,mode,key):
    result= ''
    if mode == 'd':
      key = -key

    for letter in text :
        letter = letter.lower()
        if not letter == " ":
            index = letters.find(letter)
            if index == -1:
                result += letter
            else:
                new_index = index + key
                if new_index >= num_leters:
                    new_index -= num_leters
                elif new_index<0:
                    new_index += num_leters
                result += letters[new_index]
    return result
#
# def encrypt(plaintext, key):
#     ciphertext = ''
#     for letter in plaintext:
#         letter= letter.lower()
#         if not letter == " ":
#             index  = letters.find(letter)
#             if index == -1:
#                 ciphertext += letter
#             else:
#                 new_index = index+key
#                 if new_index >= num_leters:
#                     new_index -= num_leters
#                 ciphertext += letters[new_index]
#     return ciphertext
#
# def decrypt(ciphertext, key):
#     message = ''
#     for letter in ciphertext:
#         letter= letter.lower()
#         if not letter == " ":
#             index  = letters.find(letter)
#             if index == -1:
#                 ciphertext += letter
#             else:
#                 new_index = index-key
#                 if new_index < 0:
#                     new_index += num_leters
#                 message += letters[new_index]
#     return message

print()
print("*** CEASER CIPHER PROGRAM ***")
print()

print("Do you want to encrypt or decrypt")
ui = input("e/d  ").lower()
print()



if(ui == 'e'):
    print("Encryption selected")
    print()
    key = int(input("Enter the key :  "))
    text = input("Enter th message :  ")
    ciphertext = encrypt_decrypt(text,ui,key)
    print(f"ciphertext :  {ciphertext}")

elif (ui == 'd'):
    print("Decryption selected")
    print()
    key = int(input("Enter the key"))
    text = input("Enter th ciphertext")
    plaintext = encrypt_decrypt(text,ui, key)
    print(f"plainntext :  {plaintext}")

