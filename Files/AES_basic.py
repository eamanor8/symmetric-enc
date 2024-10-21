from Crypto.Cipher import AES
from binascii import unhexlify

key = b'\x01\x23\x45\x67\x89\xab\xcd\xef\x01\x23\x45\x67\x89\xab\xcd\xef'+ \
b'\x01\x23\x45\x67\x89\xab\xcd\xef\x01\x23\x45\x67\x89\xab\xcd\xef'

text1 = b'This is a Test 1'
print('Original:	', text1.hex())

aescipher = AES.new(key, AES.MODE_ECB)

encrypted_text1 = aescipher.encrypt(text1)

print('Encrypted:	', encrypted_text1.hex())

decrypted_text1 = aescipher.decrypt(encrypted_text1)

print('Decrypted:	', decrypted_text1.hex())
print ("Decrypted Data - ["+decrypted_text1.decode("utf-8")+"]")
