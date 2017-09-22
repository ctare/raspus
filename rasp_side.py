import requests
import time

while True:
    try:
        requests.get("http://google.com", timeout=5)
        print("connected")
    except requests.exceptions.ConnectionError:
        print("no network")
    except requests.exceptions.ReadTimeout:
        print("timeout")
    time.sleep(1)
