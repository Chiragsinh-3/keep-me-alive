#!/usr/bin/env python3
import requests
import datetime

def ping_backend():
    urls = [
        "https://pageplaza.onrender.com/ping",
        "https://brainwave-ehho.onrender.com/ping"
    ]
    for url in urls:
        try:
            now = datetime.datetime.now().isoformat(sep=' ', timespec='seconds')
            print(f"{now}: Pinging {url}")
            response = requests.get(url, timeout=30)
            print(f"Response: {response.status_code}")
            if response.status_code == 200:
                print("✅ Backend is alive")
            else:
                print(f"⚠️ Unexpected status code: {response.status_code}")
        except Exception as e:
            print(f"❌ Error pinging {url}: {e}")

if __name__ == "__main__":
    ping_backend()
