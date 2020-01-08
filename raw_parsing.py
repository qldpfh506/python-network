{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from scapy.all import *\n",
    "from struct import *\n",
    "#from pcapfile import savefile\n",
    "\n",
    "import re\n",
    "import zlib\n",
    "import geoip2.database\n",
    "import os, subprocess\n",
    "import optparse, zipfile, sys\n",
    "import xml.etree.ElementTree as ET\n",
    "\n",
    "data = './dl_test.pcap'\n",
    "a = rdpcap(data)\n",
    "\n",
    "sessions = a.sessions()\n",
    "\n",
    "reader = geoip2.database.Reader('GeoLite2-City.mmdb')\n",
    "\n",
    "#global header\n",
    "g_pattern = \"=IHHIIII\"\n",
    "g_pattern_size = struct.calcsize(g_pattern)\n",
    "\n",
    "pcap_file = open(data, \"rb\")\n",
    "gheader = pcap_file.read(g_pattern_size)\n",
    "\n",
    "magic_num, v_major, v_minor, tz, flags, snaplen, network = struct.unpack(g_pattern, gheader)\n",
    "\n",
    "print(magic_num, v_major, v_minor, tz, flags, snaplen, network)\n",
    "\n",
    "#packet header\n",
    "\n",
    "p_pattern = \"=IIII\"\n",
    "p_pattern_size = struct.calcsize(p_pattern)\n",
    "\n",
    "pcap_file = open(data, \"rb\")\n",
    "pheader = pcap_file.read(p_pattern_size)\n",
    "\n",
    "ts_sec, ts_usec, incl_len, orig_len = struct.unpack(p_pattern, pheader)\n",
    "\n",
    "print(ts_sec, ts_usec, incl_len, orig_len)\n",
    "\n",
    "\n",
    "#packet body\n",
    "capfile = savefile.load_savefile(testcap, verbose = True)\n",
    "print(capfile)\n",
    "print(capfile.packets[0].packet.src)\n",
    "print(capfile.packets[0].packet.payload) #hex string snipped\n",
    "pkt = capfile.packets[0]\n",
    "pkt.raw()\n",
    "pkt.timestamp\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
