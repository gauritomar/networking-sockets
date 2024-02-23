import netifaces as ni

def get_router_ip():
    try:
        gateway = ni.gateways()['default'][ni.AF_INET][0]
        return gateway
    except KeyError:
        return None

router_ip = get_router_ip()
print("Router's IP Address:", router_ip)
