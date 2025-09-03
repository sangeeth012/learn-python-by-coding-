alphabet =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]

def encrypt(text,shift):
    data =""
    for letter in text:
        number = alphabet.index(letter)
        encrypted_data = number + shift
        data += alphabet[encrypted_data]
    print(f"encrypted_data..= {data}")
def decrypt(text,shift):
    data =""
    for letter in text:
        number = alphabet.index(letter)
        decrypted = number - shift
        data += alphabet[decrypted]
    print(f"encrypted_data..= {data}")

text = input("enter your message ..")
shift = int(input("please enter the shit number.."))
direction = int(input("Enter zero for encrypt = '0',or enter one for decrypt ='1' "))
if direction == 0:
    encrypt(text, shift)
direction = int(input("Enter zero for encrypt = '0',or enter one for decrypt ='1' "))
text = input("enter your message ..")
shift = int(input("please enter the shit number.."))
if direction == 1:
    decrypt(text, shift)
else:
    print("Invalid option. Please enter '0' or '1'.")