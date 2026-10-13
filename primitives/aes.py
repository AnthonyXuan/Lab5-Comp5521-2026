import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def encrypt(key, message):
    # randomly generate a 128-bit initialization vector (iv)
    iv = os.urandom(16)

    # construct an AES-OFB cipher with the given key and iv
    cipher = Cipher(algorithms.AES(key), modes.OFB(iv))

    # get the encryptor
    encryptor = cipher.encryptor()

    # encrypt the message and get the ciphertext
    # OFB mode does not require padding
    ciphertext = encryptor.update(message) + encryptor.finalize()

    return (iv, ciphertext)


def decrypt(key, iv, ciphertext):
  
    # construct a cipher with the key and iv
    cipher = Cipher(algorithms.AES(key), modes.OFB(iv))

    # get the decryptor
    decryptor = cipher.decryptor()

    # decrypt the message and get the plaintext
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    return plaintext


def main():
    # randomly generate a 256-bit key
    key = os.urandom(32)

    # encrypt a message 'This is COMP5521.', getting the ciphertext
    iv, ciphertext = encrypt(key, b'We are PolyU, Together We Excel!')
    print(f'ciphertext:\t {ciphertext.hex()}')

    # decrypt the ciphertext, getting the plaintext
    plaintext = decrypt(key, iv, ciphertext)
    print(f'plaintext:\t {plaintext.decode("utf-8")}')


if __name__ == '__main__':
    main()
