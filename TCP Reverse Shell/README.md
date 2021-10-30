## Attacker
```netstat -antp | grep 8080```

## Victim
```Shell> cd*New Folder```
```Shell> scan 192.168.162.128:21,23,80,8080,8888```
- With these options:
  - File Transfer
  - Target Directory Navigation
  - Low Level Port Scanner

## Exercise 1
- When we hit enter key multiple times our shell breaks due to improper handling of empty string. The simplest way is by adding a new line in our server code saying if the user input was empty string ' ' then we do nothing or we may send a trivial command like "whoami" ????????????????When we hit enter key multiple times our shell breaks due to improper handling of empty string. The simplest way is by adding a new line in our server code saying if the user input was empty string ' ' then we do nothing or we may send a trivial command like "whoami" ????????????????

## Exercise 2
- Update your client and server scripts where you can push a file from the attacker machine down to the target machine.
  - Try to take an advantage of the 'transfer' function 
  - Add a new "if" statement like 'download' 

## Exporting To EXE
```pip install pyinstaller```
```pyinstaller -F -w client.py```
