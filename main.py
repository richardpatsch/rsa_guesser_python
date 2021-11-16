import rsa


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.


publicKey, privateKey = rsa.newkeys(128)


def encrypt(message, public_key):
    encrypted_message = rsa.encrypt(message.encode(), public_key)
    print(message)
    print(encrypted_message)


    return encrypted_message


def decrypt(encrypted_message, private_key):
    decrypted_message = rsa.decrypt(encrypted_message, private_key).decode()
    print(encrypted_message)
    print(decrypted_message)
    return decrypted_message


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('public key: ' + str(publicKey))
    print('private key: ' + str(privateKey))
    encryped_message = encrypt("hallo", publicKey)
    decrypt(encryped_message, privateKey)
    new_public, new_private = rsa.newkeys(128)
    decrypt(encryped_message, new_private)

