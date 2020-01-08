from scapy.all import *

import re
import zlib

data = './dl_test.pcap'
a = rdpcap(data)

sessions = a.sessions()

for session in sessions:
    for packet in sessions[session]:
        try:
            if packet[TCP].dport == 80 or packet[TCP].sport == 80:
                print(packet.summary())
        except:
            pass

print("End")
