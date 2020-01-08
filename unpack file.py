{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "32512"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from scapy.all import *\n",
    "\n",
    "import re\n",
    "import struct\n",
    "import zlib\n",
    "import os\n",
    "\n",
    "data = './dl_test.pcap'\n",
    "\n",
    "def parse_capabilities(raw_data):\n",
    "    \"\"\"Parse capabilities data.\"\"\"\n",
    "    capabilities = {}\n",
    "    raw_int = _raw_to_int(raw_data)\n",
    "\n",
    "    capabilities['max_policies'] = raw_int[3]\n",
    "    capabilities_values = struct.unpack('<HHIIHH', bytearray(\n",
    "                                        raw_int[4:20]))\n",
    "    capabilities_names = ('max_limit_value', 'min_limit_value',\n",
    "                          'min_correction_time', 'max_correction_time',\n",
    "                          'min_reporting_period', 'max_reporting_period')\n",
    "    _add_to_dict(capabilities, capabilities_values, capabilities_names)\n",
    "    capabilities['domain_id'] = DOMAINS_REV[raw_int[20] & 0x0F]\n",
    "    power_domain = POWER_DOMAIN_REV[raw_int[20] & 0x80]\n",
    "    capabilities['power_domain'] = power_domain\n",
    "\n",
    "    return capabilities \n"
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
