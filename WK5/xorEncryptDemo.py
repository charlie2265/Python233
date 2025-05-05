# xorEncryption - take text convert to binary

import base64
from itertools import izip, cycle

def xor_crypt_string(data, key="MHCCSaints", encode=False, decode=False):
    if decode:
        data = base64.decodestring(data)
    xored = ''.join(chr(ord(x) ^ ord(y)) for (x,y) in izip(data, cycle(key)))
    
    if encode:
        return base64.encodestring(xored).strip()
    return xored

secret_data = "At Dawn W3 Ride! 123"

print ("The cypher test is:")
print (xor_crypt_string(secret_data, encode= True))

print("the plain text is:")
print (xor_crypt_string(xor_crypt_string(secret_data, encode=True), decode=True))





# e = base64.b64encode("text")
# print(e)

# d = base64.b64decode(e)
# print(d)

# Python3 of above code. 
# e = base64.b64encode(b"text")  # Convert the string to bytes by adding 'b' prefix
# print(e.decode())  # Decode the bytes to a string