#!/usr/bin/env python3
import requests
import datetime
import time

def ping_backend():
   
    urls = [
        "https://pageplaza.onrender.com/ping",
        "https://brainwave-ehho.onrender.com/ping"
    ]
    while True:
        for url in urls:
            try:
                print(f"{datetime.datetime.now()}: Pinging {url}")
                response = requests.get(url, timeout=30)
                print(f"Response: {response.status_code}")
                if response.status_code == 200:
                    print("Backend is alive")
                else:
                    print(f"⚠️ Unexpected status code: {response.status_code}")
            except Exception as e:
                print(f"Error: {e}")
        print("Waiting 14 minutes before next ping...")
        time.sleep(14 * 60)

if __name__ == "__main__":
    ping_backend()  # This will ping both URLs every 14 minutes, forever