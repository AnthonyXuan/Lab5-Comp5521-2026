from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec


def sign(sk, message):
    # sign the message using private key (sk)
    signature = sk.sign(message, ec.ECDSA(hashes.SHA256()))
    return signature


def verify(pk, signature, message):
    # verify the signature using public key (pk)
    try:
        pk.verify(signature, message, ec.ECDSA(hashes.SHA256()))
    except: 
        # signature is invalid
        return "false"
    else:
        # signature is valid
        return "true"


def main():
    # generate a private key using SECP384R1 curve
    private_key = ec.generate_private_key(ec.SECP384R1())

    # derive the public key from the private key
    public_key = private_key.public_key()

    message = b'We are PolyU, Together We Excel!'

    # sign the message, getting the signature
    signature = sign(private_key, message)
    print(f'signature:\n{signature.hex()}\n')

    # signature = ""
    # verify the signature
    ver_res = verify(public_key, signature, message)
    print(f'verification: {ver_res}')


if __name__ == '__main__':
    main()
