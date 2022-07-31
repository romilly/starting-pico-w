#!/usr/bin/env bash
mpremote exec "import machine;machine.bootloader()" 2> /dev/null
echo 'blatted - waiting 5 secs'
sleep 5
cp rp2-pico-w-20220727-unstable-v1.19.1-216-g45ab801c3.uf2 /media/$USER/RPI-RP2
echo 'uPython copied - waiting 5 secs'
sleep 5