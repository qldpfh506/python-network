{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import sys\n",
    "from scapy.all import sr1, IP, ICMP\n",
    "\n",
    "packet = IP(dst = sys.argv[1])/ICMP()\n",
    "print(\"+---------- Sending Packet INFO\")\n",
    "packet.show()\n",
    "result = sr1(packet)\n",
    "if result:\n",
    "    print(\"+---------- Receiving Packet INFO\")\n",
    "    result.show()"
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
