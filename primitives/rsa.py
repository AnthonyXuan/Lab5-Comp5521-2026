from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.backends import default_backend as crypto_default_backend


def key_gen():
    # generate the private key
    private_key = rsa.generate_private_key(backend=crypto_default_backend(),
                                           public_exponent=65537,
                                           key_size=2048)
  
    # derive the public key
    public_key = private_key.public_key()

    return (private_key, public_key)


def encrypt(pk, message):
    # encrypt the message using the public key
    # the message should be padded
    ciphertext = pk.encrypt(
        message,
        padding.OAEP(padding.MGF1(algorithm=hashes.SHA256()), hashes.SHA256(),
                     None))
    return ciphertext


def decrypt(sk, ciphertext):
    # decrypt the ciphertext using the private key
    # the decrypted plaintext should be unpadded
    plaintext = sk.decrypt(
        ciphertext,
        padding.OAEP(padding.MGF1(algorithm=hashes.SHA256()), hashes.SHA256(),
                     None))
    return plaintext


def main():
    # generate the keypair: private key (sk) and public key (pk) 
    sk, pk = key_gen()

    # encrypt the message 'This is COMP5521' under RSA, getting the ciphertext
    ciphertext = encrypt(pk, b'We are PolyU, Together We Excel!')
    print(f'ciphertext:\t {ciphertext.hex()}')

    # decrypte the ciphertext, getting the plaintext
    plaintext = decrypt(sk, ciphertext)
    print(f'plaintext:\t {plaintext.decode("utf-8")}')


if __name__ == '__main__':
    main()
