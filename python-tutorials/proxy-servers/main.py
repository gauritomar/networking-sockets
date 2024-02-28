import requests
import json

with open('500_proxies.json') as f:
    data = json.load(f)['data']

proxies = []

for proxy_info in data:
    proxy_ip = proxy_info['ip']
    proxy_port = proxy_info['port']
    if proxy_ip and proxy_port:
        proxy = f"{proxy_ip}:{proxy_port}"
        proxies.append(proxy)


for proxy in proxies:
    try:
        response = requests.get("https://ipinfo.io/json", proxies={'https': proxy}, timeout=5)
        if response.status_code == 200:
            print(f"Proxy {proxy} works!")
            print(response.text)
            break  # Exit loop if a working proxy is found
    except Exception as e:
        print(f"Proxy {proxy} failed: {e}")
