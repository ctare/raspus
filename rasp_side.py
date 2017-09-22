import requests
import time

while True:
    try:
        requests.get("http://ctare.cloudapp.net:8000/bus/hachioji", timeout=5)
        print("connected")
    except requests.exceptions.ConnectionError:
        print("no network")
    except requests.exceptions.ReadTimeout:
        print("timeout")
    time.sleep(1)
