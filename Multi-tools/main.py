import os
import pyfiglet
import socket
import threading
import concurrent.futures
import datetime
import argparse
import requests
from colorama import init, Fore
from pystyle import Colors, Colorate, Center, System
import uuid
import tempfile
import subprocess
import random
import string
import datetime
import base64

def clear_screen():
    # Vérifie le système d'exploitation pour nettoyer l'écran
    os.system('cls' if os.name == 'nt' else 'clear')



def ip_lookup():
    print(f"""{Fore.MAGENTA}
                ,
       ,   |\ ,__
       |\   \/   `.
       \ `-.:.     `\\
        `-.__ `\=====|
           /=`'/   ^_\\
         .'   /\   .=)
      .-'  .'|  '-(/_|
    .'  __(  \  .'`
   /_.'`  `.  |`
            \ |
             |/  "No system is safe"
██╗██████╗     ██╗      ██████╗  ██████╗ ██╗  ██╗██╗   ██╗██████╗ 
██║██╔══██╗    ██║     ██╔═══██╗██╔═══██╗██║ ██╔╝██║   ██║██╔══██╗
██║██████╔╝    ██║     ██║   ██║██║   ██║█████╔╝ ██║   ██║██████╔╝
██║██╔═══╝     ██║     ██║   ██║██║   ██║██╔═██╗ ██║   ██║██╔═══╝ 
██║██║         ███████╗╚██████╔╝╚██████╔╝██║  ██╗╚██████╔╝██║     
╚═╝╚═╝         ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝     
                    """)
    
    def get_ip_info(ip):
        try:
            response = requests.get(f"https://ipinfo.io/{ip}/json")
            data = response.json()

            if 'error' in data:
                print(f"Erreur : {data['error']['message']}")
                return

            latitude, longitude = data.get('loc', '0,0').split(',')
            maps_url = f"https://www.google.com/maps/@{latitude},{longitude},15z"

            # Vérification si l'IP est un VPN
            is_vpn = "VPN" in data.get('org', '')

            print("\nInformations sur l'IP :")
            print(f"IP : {data.get('ip', 'N/A')}")
            print(f"Ville : {data.get('city', 'N/A')}")
            print(f"Région : {data.get('region', 'N/A')}")
            print(f"Code postal : {data.get('postal', 'N/A')}")
            print(f"Pays : {data.get('country', 'N/A')}")
            print(f"Fournisseur : {data.get('org', 'N/A')}")
            print(f"Localisation : {data.get('loc', 'N/A')}")
            print(f"Voir sur Google Maps : {maps_url}")
            print(f"L'IP est sous VPN : {'Oui' if is_vpn else 'Non'}")

        except requests.exceptions.RequestException as e:
            print(f"Erreur lors de la récupération des informations : {e}")

    ip = input("Entrez l'adresse IP à rechercher : ")
    get_ip_info(ip)



def port_scanner():
    ip = input("Enter the target IP address to scan: ")
    nport = input("Enter the port range (default = 1-1000, 'all' for all ports): ")

    if nport == "":
        start = 1
        end = 1000
    elif nport == "all":
        start = 1
        end = 65535
    else:
        start, end = nport.split("-")
        start = int(start)
        end = int(end)

    print("-" * 70)
    print("[Dev by NewCode]")
    print("Github : https://github.com/newcode255/NewCodeScanner.git")
    print("""
                ,
       ,   |\ ,__
       |\   \/   `.
       \ `-.:.     `\\
        `-.__ `\=====|
           /=`'/   ^_\\
         .'   /\   .=)
      .-'  .'|  '-(/_|
    .'  __(  \  .'`
   /_.'`  `.  |`
            \ |
             |/  "No system is safe"
██████╗  ██████╗ ██████╗ ████████╗    ███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ 
██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝    ██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
██████╔╝██║   ██║██████╔╝   ██║       ███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
██╔═══╝ ██║   ██║██╔══██╗   ██║       ╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
██║     ╚██████╔╝██║  ██║   ██║       ███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝       ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
                                                                                                               
    
    """)
    print("\n")

    def date_time():
        return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    print_lock = threading.Lock()

    targetip = socket.gethostbyname(ip)

    print("[Scanning Target ]- {} ({})".format(ip, targetip))
    print("[Scan started ]- [{}]".format(date_time()))

    print("\n      |Ip|\t\t|Open Port|\t\t|State|")
    print("-" * 55)

    def scan(ip, port):
        scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        scanner.settimeout(1)

        try:
            scanner.connect((ip, port))
            scanner.close()

            with print_lock:
                print("{}\t\t{}\t\tOpen".format(targetip, port))

        except:
            pass

    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(start, end + 1):
            executor.submit(scan, ip, port)

    print("\n[Scan finished! Thanks for using - ][{}]".format(date_time()))
    print("-" * 70)







def nitro_gen():
    print("""
                ,
       ,   |\ ,__
       |\   \/   `.
       \ `-.:.     `\\
        `-.__ `\=====|
           /=`'/   ^_\\
         .'   /\   .=)
      .-'  .'|  '-(/_|
    .'  __(  \  .'`
   /_.'`  `.  |`
            \ |
             |/  "No system is safe"

███╗   ██╗██╗████████╗██████╗  ██████╗      ██████╗ ███████╗███╗   ██╗
████╗  ██║██║╚══██╔══╝██╔══██╗██╔═══██╗    ██╔════╝ ██╔════╝████╗  ██║
██╔██╗ ██║██║   ██║   ██████╔╝██║   ██║    ██║  ███╗█████╗  ██╔██╗ ██║
██║╚██╗██║██║   ██║   ██╔══██╗██║   ██║    ██║   ██║██╔══╝  ██║╚██╗██║
██║ ╚████║██║   ██║   ██║  ██║╚██████╔╝    ╚██████╔╝███████╗██║ ╚████║
╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝      ╚═════╝ ╚══════╝╚═╝  ╚═══╝                                                                      
        """)
    def generate_nitro_code():
        return ''.join(random.choices(string.ascii_letters + string.digits, k=16))

    def check_nitro_code(code):
        url = f"https://discord.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"
        response = requests.get(url)
        return response.status_code == 200

    while True:
        nitro_code = generate_nitro_code()
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        if check_nitro_code(nitro_code):
            print(f"[{now}] [✔] | Status: Valid | Nitro: {nitro_code}")
        else:
            print(f"[{now}] [x] | Status: Invalid | Nitro: {nitro_code}")




def token_finder():
    print("""
            ,
       ,   |\ ,__
       |\   \/   `.
       \ `-.:.     `\\
        `-.__ `\=====|
           /=`'/   ^_\\
         .'   /\   .=)
      .-'  .'|  '-(/_|
    .'  __(  \  .'`
   /_.'`  `.  |`
            \ |
             |/  "No system is safe"
          
██╗██████╗     ████████╗ ██████╗     ████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗
██║██╔══██╗    ╚══██╔══╝██╔═══██╗    ╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║
██║██║  ██║       ██║   ██║   ██║       ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║
██║██║  ██║       ██║   ██║   ██║       ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║
██║██████╔╝       ██║   ╚██████╔╝       ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║
╚═╝╚═════╝        ╚═╝    ╚═════╝        ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝
                                                                                 """)
    print("Cet outils permet de trouver la moitiée d'un token grace a une id discord encoder en base64")
    print("-" * 70)
    def encode_to_base64(id_str):
        # Convertir l'ID en bytes
        id_bytes = id_str.encode('utf-8')
        # Encoder en Base64
        encoded_bytes = base64.b64encode(id_bytes)
        return encoded_bytes.decode('utf-8')

    def decode_from_base64(encoded_str):
        try:
            # Décoder la chaîne Base64
            decoded_bytes = base64.b64decode(encoded_str)
            return decoded_bytes.decode('utf-8')
        except Exception as e:
            return f"Erreur lors du décodage : {e}"

    id_input = input("Quel ID voulez-vous encoder et décoder ? ")
    
    # Encoder en Base64
    encoded_output = encode_to_base64(id_input)
    print(f"ID encodé en Base64 : {encoded_output}")

    # Décoder immédiatement pour montrer le processus
    decoded_output = decode_from_base64(encoded_output)
    print(f"ID décodé depuis Base64 : {decoded_output}")
    print("-" * 70)















def display_menu():
    print(f"""{Fore.BLUE}
    
            ,
       ,   |\ ,__
       |\   \/   `.
       \ `-.:.     `\\
        `-.__ `\=====|
           /=`'/   ^_\\
         .'   /\   .=)
      .-'  .'|  '-(/_|
    .'  __(  \  .'`
   /_.'`  `.  |`
            \ |
             |/  "No system is safe"

             .__  .__           .__  .__
___  _______  |  | |  |__ _____  |  | |  | _____
\  \/ /\__  \ |  | |  |  \\\\__  \ |  | |  | \__  \\
 \   /  / __ \|  |_|   Y  \/ __ \|  |_|  |__/ __ \_
  \_/  (____  /____/___|  (____  /____/____(____  /
            \/          \/     \/               \/
               Author:  Forbidden
               Version: v1.0
""")
    options = [
        "1. IP-Lookup",
        "2. Port-Scanner",
        "3. Token Finder",
        "4. Nitro-Gen"
    ]
    
    # Affichage en 3 colonnes et 2 par colonne
    for i in range(0, len(options), 3):
        line = "\t".join(options[i:i+3])
        print(line)

def main():
    while True:
        clear_screen()  # Nettoyer l'écran à chaque boucle
        print("\nMenu Multitools")
        display_menu()

        choice = input("Choisissez une option : ")

        if choice == '1':
            clear_screen()
            ip_lookup()
            # Demander à l'utilisateur s'il veut retourner au menu ou quitter
            again = input("\nVoulez-vous retourner au menu ? (o/n) : ")
            if again.lower() != 'o':
                print("Au revoir!")
                break
        elif choice == '2':
            clear_screen()
            port_scanner()  # Remplace par ton implémentation
            again = input("\nVoulez-vous retourner au menu ? (o/n) : ")
            if again.lower() != 'o':
                print("Au revoir!")
                break
        elif choice == '3':
            clear_screen()
            token_finder()  # Remplace par ton implémentation
            again = input("\nVoulez-vous retourner au menu ? (o/n) : ")
            if again.lower() != 'o':
                print("Au revoir!")
                break
        elif choice == '4':
            clear_screen()
            nitro_gen()  # Remplace par ton implémentation
            again = input("\nVoulez-vous retourner au menu ? (o/n) : ")
            if again.lower() != 'o':
                print("Au revoir!")
                break
        elif choice == '5':
            clear_screen()
            again = input("\nVoulez-vous retourner au menu ? (o/n) : ")
            if again.lower() != 'o':
                print("Au revoir!")
                break
        else:
            print("Choix invalide, veuillez réessayer.")
            input("Appuyez sur Entrée pour continuer...")  # Attendre que l'utilisateur appuie sur Entrée


if __name__ == "__main__":
    main()
