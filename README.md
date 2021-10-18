# Python Scripts
A Collection of Python Scripts.

## Linux MAC Changer
```python linux_MAC_changer.py --interface eth0 --mac 12:11:11:11:11:11```
- First octet of the new MAC should be even (because of Unicast)

## Network Scanner
```python network_scanner.py --target 172.25.12.34/24```
- Use ```arp``` as a filter to check output in Wireshark

## ARP Spoofer
```python arp_spoofer.py --target 172.25.12.21 --gateway 172.25.12.1```
- Use ```echo 1 > /proc/sys/net/ipv4``` in attacker machine to route victim traffic to gateway

## Packet Sniffer
```python packet_sniffer.py --interface Ethernet```
- Use ```pip install scapy_http```
- Turn off all proxy
- Combine this script with Arp Spoofer

## ARP Spoof Detector
```python arp_spoof_detector.py```

## Maleware - Wifi Passwords
```python packet_sniffer.py --interface Ethernet```
- Set "Less secure apps" for gmail account
- It will send all wifi credentials on laptopn to an email address
