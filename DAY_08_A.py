from email import message


command = print(input('Type \'encode\' to encrypt, type \'decode\' to decrypt:'))

message = print(input('Type your message'))

shifts = print(input('Type the shift number:'))

if command == 'encode':
    print([*message])
