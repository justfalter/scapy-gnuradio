## This file is part of Scapy
## See http://www.secdev.org/projects/scapy for more information
## Copyright (C) Airbus DS CyberSecurity
## Authors: Jean-Michel Picod, Arnaud Lebrun, Jonathan Christofer Demay
## This program is published under a GPLv2 license

"""
Gnuradio layers, sockets and send/receive functions.
"""

from scapy_gnuradio.layers.ZWave import *
from scapy_gnuradio.layers.dot15d4 import *
from scapy_gnuradio.layers.bluetooth4LE import *
from scapy_gnuradio.layers.wmbus import *


class GnuradioPacket(Packet):
    name = "Gnuradio header"
    fields_desc = [
        ByteField("proto", 0),
        X3BytesField("reserved1", 0),
        IntField("reserved2", 0)
    ]


## Z-Wave
bind_bottom_up(GnuradioPacket, ZWave, proto=1)
bind_top_down(GnuradioPacket, ZWaveReq, proto=1)

## ZigBee
bind_layers(GnuradioPacket, Dot15d4FCS, proto=2)

## Bluetooth 4 LE
bind_layers(GnuradioPacket, BTLE, proto=3)

## WMBus
bind_layers(GnuradioPacket, WMBus, proto=4)

## Dash7
#bind_layers(GnuradioPacket, Dash7, proto=5)

conf.l2types.register(148, GnuradioPacket)
