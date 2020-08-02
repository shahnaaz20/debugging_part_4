def encrypt(message):
    ascii_message = [ord(char)+3 for char in message]
    encrypt_message = [ chr(char) for char in ascii_message]  
    return(''.join(encrypt_message))
def decrypt(message):
    ascii_message = [ord(char)-3 for char in message]
    decrypt_message = [ chr(char) for char in ascii_message]  
    return (''.join(decrypt_message))
flag = True
while flag == True:
    choice = input("What do you want to do? 1. Encrypt a message 2. Decrypt a message  Enter `e` or `d` respectively!")
    if choice == 'e':
        message = input("Enter message to encrypt??")
        print(encrypt(message))
        break
    elif choice == 'd':
        message = input("Enter message to decrypt?")
        print(decrypt(message))
        break
    else:
        play_again = input("Do you want to try agian or Do you want to exit? (y/n)")
        if play_again == 'y':
            continue
        else:
            break