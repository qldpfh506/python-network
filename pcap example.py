{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from scapy.all import *\n",
    "\n",
    "import re\n",
    "import zlib\n",
    "\n",
    "data = './dl_test.pcap'\n",
    "a = rdpcap(data)\n",
    "\n",
    "sessions = a.sessions()\n",
    "\n",
    "for session in sessinos:\n",
    "    for packet in sessions[session]:\n",
    "        try:\n",
    "            if packet[TCP].dport == 80 or packet[TCP].sport == 80:\n",
    "                print(packet.show())\n",
    "        except:\n",
    "            pass\n",
    "        \n",
    "print(\"End\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.4.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
