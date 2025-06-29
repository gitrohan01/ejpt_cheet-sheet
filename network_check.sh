#!/bin/bash

read -p "Enter a domain name or IP address: " TARGET

x-terminal-emulator -e bash -c "ping -c 4 $TARGET; exec bash" &
x-terminal-emulator -e bash -c "traceroute $TARGET; exec bash" &
x-terminal-emulator -e bash -c "nslookup $TARGET; exec bash" &
x-terminal-emulator -e bash -c "dig $TARGET A; exec bash" &
x-terminal-emulator -e bash -c "whois $(dig +short $TARGET); exec bash" &
x-terminal-emulator -e bash -c "netstat -tulnp; exec bash" &
x-terminal-emulator -e bash -c "curl -I http://$TARGET; exec bash" &


