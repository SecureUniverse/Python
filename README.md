# Python Scripts
A Collection of Python Scripts.

## Linux MAC Changer
```python linux_MAC_changer.py --interface eth0 --mac 12:11:11:11:11:11```
- First octet of the new MAC should be even (because of Unicast)

## Network Scanner
```python network_scanner.py --target 172.25.12.34/24```
- Use 'arp' as a filter to check output in Wireshark

## ARP Spoofer
```python arp_spoofer.py --target 172.25.12.21 --gateway 172.25.12.1```
- Use 'echo 1 > /proc/sys/net/ipv4' in attacker machine to route victim traffic to gateway

## Packet Sniffer
```python packet_sniffer.py --interface Ethernet```
- Use 'pip install scapy_http'
- Turn off all proxy
- Combine this script with Arp Spoofer


## DNS Spoofer
```python dns_spoofer.py```
- Use 'pip install netfilterqueue'
- Localy (for test)
  - Use 'iptables -I INPUT -j NFQUEUE --queue-num 0'
  - Use 'iptables -I OUTPUT -j NFQUEUE --queue-num 0'
- Remotely (for dns spoofing)
  - Use 'iptables -I FORWARD -j NFQUEUE --queue-num 0' to create a queue with name of '0' for packets in 'FORWARD' chain
  - Use ARP Spoofer

