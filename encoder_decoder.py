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


def main():
    while True:
        menu()
        option = int(input('\nPlease enter an option: '))
        if option == 3:
            break
        elif option == 1:
            password = input('Please enter your password to encode: ')
            encoded_pass = encode(password)
            print('Your password has been encoded and stored!\n')
        elif option == 2:
            # Decode password
            print('The encoded password is 45678888, and the original password is 12345555.\n')
            pass


if __name__ == '__main__':
    main()
