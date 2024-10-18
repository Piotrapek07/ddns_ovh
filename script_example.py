import requests
import time
import sys

USERNAME = "admin"
PASSWORD = "admin"

def log_message(message):
    print(message)
    with open("script_log.txt", "a") as log_file:
        log_file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")

def get_public_ip():
    try:
        response = requests.get("https://api.ipify.org/")
        log_message(f"Fetched public IP address: {response.text}")
        return response.text
    except Exception as e:
        log_message(f"Error fetching IP: {e}")
        return None

def update_dns(ip):
    try:
        hostname = "admin.com"  # your domain
        url = f"https://dns.eu.ovhapis.com/nic/update?system=dyndns&hostname={hostname}&myip={ip}"

        response = requests.get(url, auth=(USERNAME, PASSWORD))
        log_message(f"OVH response: {response.text}")
        return response.text
    except Exception as e:
        log_message(f"Error updating DNS: {e}")
        return None

while True:
    try:
        public_ip = get_public_ip()
        if public_ip:
            update_response = update_dns(public_ip)

        time.sleep(1800)

    except Exception as e:
        log_message(f"An error occurred: {e}")
        time.sleep(1800)
