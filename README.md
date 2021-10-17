# Python Scripts
A Collection of Python Scripts.
## Linux MAC Changer
<b>Note:</b> First octet of the new MAC should be even (because of Unicast)<br/>
<b>Usage:</b> <i> python linux_MAC_changer.py --interface eth0 --mac 12:11:11:11:11:11</i>
## Network Scanner
<b>Note:</b> Use 'arp' as a filter to check output in Wireshark<br/>
<b>Usage:</b> <i> python network_scanner.py --target 172.25.12.34/24</i>
## Arp Spoofer
<b>Note:</b> Use 'echo 1 > /proc/sys/net/ipv4' in attacker machine to route victim traffic to gateway<br/>
<b>Usage:</b> <i> python arp_spoofer.py --target 172.25.12.21 --gateway 172.25.12.1</i>
## Packet Sniffer
<b>Note:</b> Use 'pip install scapy_http' - Turn off all proxy - Combine this script with Arp Spoofer<br/>
<b>Usage:</b> <i> python packet_sniffer.py --interface Ethernet</i>
