import requests
import time
from netifaces import AF_INET
import netifaces as ni

mydomain = str  # domain for example meme.me


def update_a_record(cname: str, ip: str) -> None:  # Will update GoDaddy api with the specified  cname

    url = "https://api.godaddy.com/v1/domains/<yourdomain>/records/A/{}".format(cname)

    payload = "[  {    \"data\": \"" + ip + "\",    \"port\": 1,    \"priority\": 0,    \"protocol\": \"string\"," \
                                            "    \"service\": \"string\",    \"ttl\": 3600,    \"weight\": 0  }]"
    headers = {
        'accept': "application/json",
        'Content-Type': "application/json",
        'Authorization': "",  # add it
    }

    requests.request("PUT", url, data=payload, headers=headers)


ppp_ip = ni.ifaddresses('ppp0')[AF_INET][0]['addr']  # Will get PPP interface ipv4

while True:
    update_a_record(cname='Server', ip=ppp_ip)
    update_a_record(cname='Myname', ip=ppp_ip)
    time.sleep(600)
