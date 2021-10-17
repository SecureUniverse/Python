# PythonScripts
A Collection of Python Script
## Linux_MAC_Changer
First octet of the new MAC should be even (because of Unicast)<br/>
<b>Usage:</b> <i>> python Linux_MAC_Changer.py --interface eth0 --mac 12:11:11:11:11:11</i>
## Network_Scanner
Use 'arp' as a filter to check output in Wireshark<br/>
<b>Usage:</b> <i>> python Network_Scanner.py --target 172.25.12.34/24</i>
## Arp_Spoofer
Use 'echo 1 > /proc/sys/net/ipv4' in attacker machine to route victim traffic to gateway<br/>
<b>Usage:</b> <i>> python MAC_Changer.py --target 172.25.12.21 --gateway 172.25.12.1</i>
