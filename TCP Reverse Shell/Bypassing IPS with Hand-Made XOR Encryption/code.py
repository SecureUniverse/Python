import string
import random

key = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + '^!\$%&/()=?{[]}+~#-_.:,;<>|\\') for _ in range(0, 1024))
print(key)
print("\n" + "Key length = " + str(len(key)))

message = 'ipconfig'
print("Msg: " + message + '\n')

def str_xor(s1, s2):
    return "".join([chr(ord(c1) ^ ord(c2)) for (c1, c2) in zip(s1, s2)])

enc = str_xor(message, key)
print("Encrypted message is " + "\n" + enc + "\n")

dec = str_xor(enc, key)
print("Decryted message is " + "\n" + dec + "\n")
