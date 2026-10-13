import hashlib

msg = b'We are PolyU, Together We Excel!'

# MD5 hash
md5 = hashlib.md5()
md5.update(msg)
print('MD5 hash: \t\t' + md5.hexdigest())

# Secure hash algorithm 1
sha1 = hashlib.sha224()
sha1.update(msg)
print('SHA-1 hash: \t' + sha1.hexdigest())

# Secure hash algorithm 256
sha256 = hashlib.sha256()
sha256.update(msg)
print('SHA-256 hash: \t' + sha256.hexdigest())
