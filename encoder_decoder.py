# Paula Morales Rivera
# Menu and Encoder

# Displays menu
def menu():
    print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit')


# Encodes password
def encode(password):
    encoded_pass = ''
    for i in password:
        # Increments item by three
        encoded_num = int(i) + 3
        # If the encoded_num total is greater than three, reduce
        if encoded_num > 9:
            encoded_num = encoded_num - 10
            encoded_pass += str(encoded_num)
        else:
            encoded_pass += str(encoded_num)
    return encoded_pass

# decodes password Noel Mendez
def decode(encoded_password):
    decoded_pass = ''
    for i in encoded_password:
        # Decrements item by three
        decoded_num = (int(i) - 3) % 10
        decoded_pass += str(decoded_num)
    return decoded_pass


def main():
    while True:
        menu()
        option = int(input('\nPlease enter an option: '))
        if option == 3:
            break
        elif option == 1:
            password = input('Please enter your password to encode: ')            encoded_pass = encode(password)
            print('Your password has been encoded and stored!\n')

        elif option == 2:
            # decodes password Noel Mendez
            encoded_password = input('Please enter the password to decode: ')
            decoded_pass = decode(encoded_password)
            print('The decoded password is:', decoded_pass, 'and the original password is', encoded_password + '.\n')

if __name__ == '__main__':
    main()
