import requests
from pprint import pprint

def get_ip_adress():

    """Get the public IP address."""
    url = "https://api.ipify.org/?format=json"
    return requests.get(url).json()['ip']

def get_location(ip):
    
    """Get location information based on IP address."""
    url = f"https://ipinfo.io/{ip}/geo"
    return requests.get(url).json()

def main():
    ip = get_ip_adress()
    location = get_location(ip)
    pprint(location)

if __name__=="__main__":
    main()