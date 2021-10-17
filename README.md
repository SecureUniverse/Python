# PythonScripts
A Collection of Python Script
## Linux_MAC_Changer
First octet of the new MAC should be even (because of Unicast)<br/>
Usage: > python Linux_MAC_Changer.py --interface eth0 --mac 12:11:11:11:11:11
## Network_Scanner
Use 'arp' as a filter to check output in Wireshark<br/>
<b>Usage:</b> > python Network_Scanner.py --target 172.25.12.34/24
## Arp_Spoofer
Use 'echo 1 > /proc/sys/net/ipv4' in attacker machine to route victim traffic to gateway<br/>
Usage: > python MAC_Changer.py --target 172.25.12.21 --gateway 172.25.12.1
