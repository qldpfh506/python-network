{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "from scapy.all import *\n",
    "\n",
    "import re\n",
    "import zlib\n",
    "import os\n",
    "data = './dl_test.pcap'\n",
    "a = rdpcap(data)\n",
    "\n",
    "os.system(\"tshark i 2 -T fields -e frame.time -e eth.src -e eth.dst -e ip.src -e ip.dst -e ip.proto -e tcp.len -e _ws.col.Info -w data.pcap > data.csv\")\n",
    "\n"
   ]
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
