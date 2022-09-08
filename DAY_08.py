from email import message
from secrets import choice
import string

print("CAESAR/'s CIPHER")

command = print(input("Type/'encode/' to encrypt, type/'decode/' to decrypt:"))

if command == 'encode':
    message = print(input('Type your message:'))
    message_split = ([*message])
    print(message_split)

elif command == 'decrypt':
    word = print(input('Type your message'))
    
