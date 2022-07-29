# Adapted From @aalaon's Gist
# https://gist.github.com/aallan/581ecf4dc92cd53e3a415b7c33a1147c

import network
import socket
import time
import struct

from secrets import SSID, PASSWORD

from machine import Pin, RTC

from network_connection import connect

NTP_DELTA = 2208988800
host = "pool.ntp.org"

led = Pin("LED", Pin.OUT)


def set_time():
    NTP_QUERY = bytearray(48)
    NTP_QUERY[0] = 0x1B
    addr = socket.getaddrinfo(host, 123)[0][-1]
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.settimeout(1)
        res = s.sendto(NTP_QUERY, addr)
        msg = s.recv(48)
    finally:
        s.close()
    val = struct.unpack("!I", msg[40:44])[0]
    t = val - NTP_DELTA    
    tm = time.gmtime(t)
    RTC().datetime((tm[0], tm[1], tm[2], tm[6] + 1, tm[3], tm[4], tm[5], 0))


def update_time():
    connect(SSID, PASSWORD)
    set_time()
    print(time.gmtime())