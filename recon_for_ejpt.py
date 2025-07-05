#!/usr/bin/env python3
import os

target = input("🔍 Enter domain or IP address: ").strip()

if not target.startswith("http"):
    http_url = f"http://{target}"
    https_url = f"https://{target}"
else:
    http_url = target
    https_url = target.replace("http://", "https://")

dirb_wordlist = "/usr/share/dirb/wordlists/common.txt"
gobuster_wordlist = "/usr/share/wordlists/dirb/common.txt"

commands = [
    f"nmap -sS -sV -Pn {target}",
    f"nmap -p- -A {target}",
    f"unicornscan -Iv -r 5000 {target}:a",
    f"whatweb {http_url}",
    f"gobuster dir -u {http_url} -w {gobuster_wordlist} -t 30",
    f"dirb {http_url} {dirb_wordlist}",
    f"arjun -u {http_url}",
    f"lbd {target}",
    f"sslscan {target}",
    f"whois {target}",
    f"dig {target} ANY +noall +answer",
    f"dnsmap {target}",
    f"amass enum -d {target}",
    f"sublist3r -d {target}"
]

# Launch each command in a new xterm window
for cmd in commands:
    os.system(f"xterm -hold -e \"{cmd}\" &")
