import requests
import re

req = requests.get("http://ipconfig.kr")
match = re.search(r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)

if match:
    out_addr = match.group(1)  # Correct way to access the matched group
    print(out_addr)
else:
    print("IP address not found")