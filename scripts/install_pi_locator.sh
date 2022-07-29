#!/usr/bin/env bash
cd ../src
mpremote cp secrets.py :secrets.py
mpremote cp network_connection.py :network_connection.py
mpremote cp -r mp/ :
mpremote cp -r pi_finder/ :
