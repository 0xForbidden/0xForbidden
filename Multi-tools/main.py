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
import requests
import whois
import socket
import subprocess
import os

def clear_screen():
    # Vérifie le système d'exploitation pour nettoyer l'écran
    os.system('cls' if os.name == 'nt' else 'clear')


import requests
import socket
import subprocess
import os



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

def rustscan_scan():
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
                 
███╗   ██╗███╗   ███╗ █████╗ ██████╗     ███████╗ ██████╗ █████╗ ███╗   ██╗
████╗  ██║████╗ ████║██╔══██╗██╔══██╗    ██╔════╝██╔════╝██╔══██╗████╗  ██║
██╔██╗ ██║██╔████╔██║███████║██████╔╝    ███████╗██║     ███████║██╔██╗ ██║
██║╚██╗██║██║╚██╔╝██║██╔══██║██╔═══╝     ╚════██║██║     ██╔══██║██║╚██╗██║
██║ ╚████║██║ ╚═╝ ██║██║  ██║██║         ███████║╚██████╗██║  ██║██║ ╚████║
╚═╝  ╚═══╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝         ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝
                                                                               
    """)

    """
    Demande à l'utilisateur une adresse IP et effectue un scan avancé avec RustScan.
    """
    print("-" * 55)
    ip = input("Entrez l'adresse IP à scanner (ex : 192.168.1.1) : ")
    print("-" * 55)
    
    try:
        # Exécuter RustScan avec les options spécifiées
        print(f"Lancement du scan RustScan pour l'IP : {ip}")
        process = subprocess.Popen([
            'rustscan',
            '-r', '1-10000',    # Plage de ports à scanner
            '-t', '1500',       # Timeout pour chaque scan
            '-a', ip,           # Adresse IP cible
            '--',               # Spécifier que les options suivantes sont pour Nmap
            '-A',               # Détection d'OS, version des services, script Nmap
            '-sC'               # Activer les scripts de Nmap (par défaut)
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Lire et afficher la sortie en temps réel
        for line in process.stdout:
            print(line, end='')

        process.stdout.close()
        process.wait()  # Attendre la fin du processus
        if process.returncode != 0:
            print(f"Erreurs de RustScan : {process.stderr.read()}")

    except Exception as e:
        print(f"Erreur lors de l'exécution de RustScan : {e}")

def userfind():
    print("""
------------------------------------------------------------------------------------------------------------------------            
------------------------------------------------------------------------------------------------------------------------            
------------------------------------------------------------------------------------------------------------------------
                                          ██████╗ ███████╗██╗███╗   ██╗████████╗
                                         ██╔═══██╗██╔════╝██║████╗  ██║╚══██╔══╝
                                         ██║   ██║███████╗██║██╔██╗ ██║   ██║   
                                         ██║   ██║╚════██║██║██║╚██╗██║   ██║   
                                         ╚██████╔╝███████║██║██║ ╚████║   ██║   
                                          ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝   
                               Dev By Sentinelle                                                                                
------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------                                           
    """)
    print("""
 ┴─────────────────────────────────────────────────────┤  OSINT  ├────────────────────────────────────────────────────┘
                                                       └─────────┘                           
    """)
    print("=" * 20)
    print("Color Blue = User Find")
    print("Color Red = User not find")
    print("=" * 20)
    pseudo = input("Entrez le pseudo à rechercher : ")

    sites = [
        {'name': 'Instagram', 'url': f'https://www.instagram.com/{pseudo}'},
        {'name': 'Twitter', 'url': f'https://twitter.com/{pseudo}'},
        {'name': 'GitHub', 'url': f'https://github.com/{pseudo}'},
        {'name': 'Reddit', 'url': f'https://www.reddit.com/user/{pseudo}'},
        {'name': 'Pinterest', 'url': f'https://www.pinterest.com/{pseudo}'},
        {'name': 'TikTok', 'url': f'https://www.tiktok.com/@{pseudo}'},
        {'name': 'Facebook', 'url': f'https://www.facebook.com/{pseudo}'},
        {'name': 'Flipboard', 'url': f'https://flipboard.com/@{pseudo}'},
        {'name': 'Linktree', 'url': f'https://linktr.ee/{pseudo}'},
        {'name': 'Minecraft', 'url': f'https://mcname.info/en/search?q={pseudo}'},
        {'name': 'Pornhub', 'url': f'https://www.pornhub.com/users/{pseudo}'},
        {'name': 'Quora', 'url': f'https://www.quora.com/profile/{pseudo}'},
        {'name': 'Soundcloud', 'url': f'https://soundcloud.com/{pseudo}'},
        {'name': 'Steam', 'url': f'https://steamcommunity.com/id/{pseudo}'},
        {'name': 'Giphy', 'url': f'https://giphy.com/channel/{pseudo}'},
        {'name': 'Habbo', 'url': f'https://www.habbo.com/api/public/users?name={pseudo}'},
        {'name': 'AudioJungle', 'url': f'https://audiojungle.net/user/{pseudo}'},
        {'name': 'GeoCaching', 'url': f'https://www.geocaching.com/p/?u={pseudo}'},
        {'name': 'Xbox', 'url': f'https://www.xboxgamertag.com/search/{pseudo}'},
        {'name': 'X-Videos', 'url': f'https://www.xvideos.com/profiles/{pseudo}'},
        {'name': 'Untappd', 'url': f'https://untappd.com/user/{pseudo}'},
        {'name': 'Twitch', 'url': f'https://twitchtracker.com/{pseudo}'},
        {'name': 'SnapChat', 'url': f'https://story.snapchat.com/s/{pseudo}'},
        {'name': 'Smule', 'url': f'https://www.smule.com/api/profile/?handle={pseudo}'},
        {'name': 'Rumbleuser', 'url': f'https://rumble.com/user/{pseudo}'},
        {'name': 'Periscope', 'url': f'https://www.periscope.tv/{pseudo}'},
        {'name': 'Revolut', 'url': f'https://revolut.me/api/web-profile/{pseudo}'},
        {'name': 'Pikabu', 'url': f'https://pikabu.ru/{pseudo}'},
        {'name': 'Picsart', 'url': f'https://picsart.com/u/{pseudo}'},
        {'name': 'Naver', 'url': f'https://blog.naver.com/{pseudo}'},
        {'name': 'MySpace', 'url': f'https://myspace.com/{pseudo}'},
        {'name': 'Bandlab', 'url': f'https://www.bandlab.com/api/v1.3/users/{pseudo}'},
        {'name': 'Bandcamp', 'url': f'https://bandcamp.com/{pseudo}'},
        {'name': 'Chess', 'url': f'https://api.chess.com/pub/player/{pseudo}'},
        {'name': 'Docker', 'url': f'https://hub.docker.com/v2/users/{pseudo}'},
        {'name': 'Kaggle', 'url': f'https://www.kaggle.com/{pseudo}'},
        {'name': 'Itch.io', 'url': f'https://itch.io/profile/{pseudo}'},
        {'name': 'Issuu', 'url': f'https://issuu.com/{pseudo}'},
        {'name': 'XNXX', 'url': f'https://www.xnxx.com/mobile/profile/{pseudo}'},
        {'name': 'Giters', 'url': f'https://giters.com/{pseudo}'},
        {'name': 'Yazawaj', 'url': f'https://www.yazawaj.com/profile/{pseudo}'},
        {'name': 'Wowhead', 'url': f'https://www.wowhead.com/user={pseudo}'},
        {'name': 'Trakt', 'url': f'https://trakt.tv/users/{pseudo}'},
        {'name': 'Fortnite', 'url': f'https://fortnitetracker.com/profile/all/{pseudo}'},
        {'name': 'Amino', 'url': f'https://aminoapps.com/u/{pseudo}'},
        {'name': 'AniWorld', 'url': f'https://aniworld.to/user/profil/{pseudo}'},
        {'name': 'AniList', 'url': f'https://anilist.co/user/{pseudo}'},
        {'name': 'AppleDiscussion', 'url': f'https://discussions.apple.com/profile/{pseudo}'},
        {'name': 'AppleDev', 'url': f'https://developer.apple.com/forums/profile/{pseudo}'},
        {'name': 'Archive.org', 'url': f'https://archive.org/details/{pseudo}'},
        {'name': '7cups', 'url': f'https://www.7cups.com/@{pseudo}'},
        {'name': '8tracks', 'url': f'https://8tracks.com/{pseudo}'},
        {'name': '7Gag', 'url': f'https://www.9gag.com/u/{pseudo}'},
        {'name': 'About.me', 'url': f'https://about.me/{pseudo}'},
        {'name': 'AllMyLinks', 'url': f'https://allmylinks.com/{pseudo}'},
        {'name': 'Asciinema', 'url': f'https://asciinema.org/~{pseudo}'},
        {'name': 'AskFm', 'url': f'https://ask.fm/{pseudo}'},
        {'name': 'Behance', 'url': f'https://www.behance.net/{pseudo}'},
        {'name': 'Bezuzyteczna', 'url': f'https://bezuzyteczna.pl/uzytkownicy/{pseudo}'},
        {'name': 'Bikemap', 'url': f'https://www.bikemap.net/en/u/user/{pseudo}'},
        {'name': 'Bitbucket', 'url': f'https://bitbucket.org/{pseudo}'},
        {'name': 'Blipfoto', 'url': f'https://www.blipfoto.com/{pseudo}'},
        {'name': 'BodyBuilding', 'url': f'https://bodyspace.bodybuilding.com/{pseudo}'},
        {'name': 'Bookcrossing', 'url': f'https://www.bookcrossing.com/mybookshelf/{pseudo}'},
        {'name': 'Buymeacoffee', 'url': f'https://buymeacoff.ee/{pseudo}'},
        {'name': 'Cgtrader', 'url': f'https://www.cgtrader.com/{pseudo}'},
        {'name': 'Championnat', 'url': f'https://www.championat.com/user/{pseudo}'},
        {'name': 'Clapper.app', 'url': f'https://clapperapp.com/{pseudo}'},
        {'name': 'Codecademy', 'url': f'https://www.codecademy.com/profiles/{pseudo}'},
        {'name': 'Codeforces', 'url': f'https://codeforces.com/profile/{pseudo}'},
        {'name': 'Coderwall', 'url': f'https://coderwall.com/{pseudo}'},
        {'name': 'Colourlovers', 'url': f'https://www.colourlovers.com/lover/{pseudo}'},
        {'name': 'Crowdin', 'url': f'https://crowdin.com/profile/{pseudo}'},
        {'name': 'Dmoj', 'url': f'https://dmoj.ca/user/{pseudo}'},
        {'name': 'DailyMotion', 'url': f'https://www.dailymotion.com/{pseudo}'},
        {'name': 'Dealabs', 'url': f'https://www.dealabs.com/profile/{pseudo}'},
        {'name': 'Disqus', 'url': f'https://disqus.com/{pseudo}'},
        {'name': 'Duolingo', 'url': f'https://www.duolingo.com/profile/{pseudo}'},
        {'name': 'Eintracht', 'url': f'https://community.eintracht.de/fans/{pseudo}'},
        {'name': 'Eyeem', 'url': f'https://www.eyeem.com/u/{pseudo}'},
        {'name': 'Flightradar24', 'url': f'https://my.flightradar24.com/{pseudo}'},
        {'name': 'Freelancer', 'url': f'https://www.freelancer.com/u/{pseudo}'},
        {'name': 'Freesound', 'url': f'https://freesound.org/people/{pseudo}'},
        {'name': 'GeekForGeeks', 'url': f'https://auth.geeksforgeeks.org/user/{pseudo}'},
    ]

    for site in sites:
        
        
        try:
            response = requests.get(site['url'])
            
            # Vérification de la réponse
            if response.status_code == 200:
                print(Fore.BLUE + f"[✔] [ user found ] sur {site['name']}: {site['url']}" + Fore.RESET)
            else:
                print(Fore.RED + f"[x] [ user not found ] sur {site['name']}" + Fore.RESET)
        except requests.exceptions.RequestException as e:
            print(Fore.RED + f"[x] [ user not found ] sur {site['name']}: {e}" + Fore.RESET)


def web():
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
                 
██╗    ██╗███████╗██████╗     ███████╗ ██████╗██████╗  █████╗ ██████╗ ██████╗ ███████╗██████╗
██║    ██║██╔════╝██╔══██╗    ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██║ █╗ ██║█████╗  ██████╔╝    ███████╗██║     ██████╔╝███████║██████╔╝██████╔╝█████╗  ██████╔╝
██║███╗██║██╔══╝  ██╔══██╗    ╚════██║██║     ██╔══██╗██╔══██║██╔═══╝ ██╔═══╝ ██╔══╝  ██╔══██╗
╚███╔███╔╝███████╗██████╔╝    ███████║╚██████╗██║  ██║██║  ██║██║     ██║     ███████╗██║  ██║
 ╚══╝╚══╝ ╚══════╝╚═════╝     ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝     ╚══════╝╚═╝  ╚═╝
                                                                                                  
    """)
    # Demander l'URL à l'utilisateur à l'intérieur de la fonction web()
    print("-" * 55)
    url = input("Entrez l'URL du site (ex : https://example.com) : ")
    print("-" * 55)
    try:
        # Vérifier si le site est accessible
        response = requests.get(url)

        # Informations sur le serveur
        server_info = response.headers.get('Server', 'Inconnu')
        ip_address = socket.gethostbyname(url.split("//")[-1].split("/")[0])
        protocol = "HTTPS" if response.url.startswith("https://") else "HTTP"

        print(f"\nInformations sur le site : {url}")
        print(f"Adresse IP : {ip_address}")
        print(f"Serveur : {server_info}")
        print(f"Protocole : {protocol}")
        # Exécuter WhatWeb pour obtenir des informations sur le site
        whatweb_scan(url)

        # Exécuter RustScan
        rustscan_scan(ip_address)

        # Exécuter Subfinder pour trouver les sous-domaines
        subfinder_scan(url)

        # Exécuter Feroxbuster pour scanner les répertoires
        feroxbuster_scan(url)

    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de l'accès au site : {e}")
    except Exception as e:
        print(f"Erreur lors de l'exécution : {e}")

def whatweb_scan(url):
    print("-" * 55)
    print(f"""{Fore.MAGENTA}
██╗    ██╗██╗  ██╗ █████╗ ████████╗██╗    ██╗███████╗██████╗     ██████╗
██║    ██║██║  ██║██╔══██╗╚══██╔══╝██║    ██║██╔════╝██╔══██╗    ╚════██╗
██║ █╗ ██║███████║███████║   ██║   ██║ █╗ ██║█████╗  ██████╔╝      ▄███╔╝
██║███╗██║██╔══██║██╔══██║   ██║   ██║███╗██║██╔══╝  ██╔══██╗      ▀▀══╝
╚███╔███╔╝██║  ██║██║  ██║   ██║   ╚███╔███╔╝███████╗██████╔╝      ██╗   
 ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚══╝╚══╝ ╚══════╝╚═════╝       ╚═╝                                                                                
    """)

    # Commande WhatWeb pour analyser le site avec l'option -v pour plus de détails
    try:
        process = subprocess.Popen([
            'whatweb',
            '-v', url
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Lire et afficher la sortie en temps réel
        for line in process.stdout:
            print(line, end='')

        process.stdout.close()
        process.wait()  # Attendre la fin du processus
        if process.returncode != 0:
            print(f"Erreurs de WhatWeb : {process.stderr.read()}")

    except Exception as e:
        print(f"Erreur lors de l'exécution de WhatWeb : {e}")

def rustscan_scan(ip_adress):
    print("-" * 55)
    

    # Commande RustScan pour scanner les ports 1-1000
    try:
        process = subprocess.Popen([
            'rustscan',
            '-a', ip_adress,
            '-r', '1-1000'
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Afficher la sortie en temps réel
        for line in process.stdout:
            print(line, end='')

        process.stdout.close()
        process.wait()  # Attendre la fin du processus
        if process.returncode != 0:
            print(f"Erreurs de RustScan : {process.stderr.read()}")

    except Exception as e:
        print(f"Erreur lors de l'exécution de RustScan : {e}")

def subfinder_scan(url):
    print("-" * 55)
    print(f"""{Fore.MAGENTA}
███████╗██╗   ██╗██████╗ ███████╗██╗███╗   ██╗██████╗ ███████╗██████╗
██╔════╝██║   ██║██╔══██╗██╔════╝██║████╗  ██║██╔══██╗██╔════╝██╔══██╗
███████╗██║   ██║██████╔╝█████╗  ██║██╔██╗ ██║██║  ██║█████╗  ██████╔╝
╚════██║██║   ██║██╔══██╗██╔══╝  ██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
███████║╚██████╔╝██████╔╝██║     ██║██║ ╚████║██████╔╝███████╗██║  ██║
╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝                                                                          
    """)
    

    # Commande Subfinder pour rechercher des sous-domaines
    try:
        process = subprocess.Popen([
            'subfinder',
            '-d', url
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Collecter la sortie
        stdout, stderr = process.communicate()

        # Vérifier si des sous-domaines ont été trouvés
        if stdout.strip():
            print(stdout)  # Afficher les résultats si des sous-domaines ont été trouvés
        else:
            print(f"[INF] Found 0 subdomains for {url}")

        process.wait()  # Attendre la fin du processus
        if process.returncode != 0:
            print(f"Erreurs de Subfinder : {stderr}")

    except Exception as e:
        print(f"Erreur lors de l'exécution de Subfinder : {e}")

def feroxbuster_scan(url):
    print("-" * 55)
    print(f"""{Fore.MAGENTA}
███████╗███████╗██████╗  ██████╗ ██╗  ██╗██████╗ ██╗   ██╗███████╗████████╗███████╗██████╗
██╔════╝██╔════╝██╔══██╗██╔═══██╗╚██╗██╔╝██╔══██╗██║   ██║██╔════╝╚══██╔══╝██╔════╝██╔══██╗
█████╗  █████╗  ██████╔╝██║   ██║ ╚███╔╝ ██████╔╝██║   ██║███████╗   ██║   █████╗  ██████╔╝
██╔══╝  ██╔══╝  ██╔══██╗██║   ██║ ██╔██╗ ██╔══██╗██║   ██║╚════██║   ██║   ██╔══╝  ██╔══██╗
██║     ███████╗██║  ██║╚██████╔╝██╔╝ ██╗██████╔╝╚██████╔╝███████║   ██║   ███████╗██║  ██║
╚═╝     ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝                                                                                                   
        """)

    

    # Récupérer le chemin complet de la wordlist depuis le répertoire de l'utilisateur
    wordlist_path = os.path.join(os.getcwd(), 'directory-list-2.3-medium.txt')
    
    # Vérifier si le fichier wordlist existe
    if not os.path.exists(wordlist_path):
        print(f"Erreur : Le fichier {wordlist_path} n'existe pas dans le répertoire courant.")
        return

    # Commande Feroxbuster avec la wordlist et l'ajout de 100 threads
    try:
        process = subprocess.Popen([
            'feroxbuster',
            '-u', url,
            '-w', wordlist_path,
            '-s', '200,301',
            '--timeout', '60',
            '-t', '100'  # Ajouter l'option -t pour utiliser 100 threads
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Lire et afficher la sortie en temps réel
        for line in process.stdout:
            print(line, end='')

        process.stdout.close()
        process.wait()  # Attendre la fin du processus
        if process.returncode != 0:
            print(f"Erreurs de Feroxbuster : {process.stderr.read()}")

    except Exception as e:
        print(f"Erreur lors de l'exécution de Feroxbuster : {e}")

def display_menu():
    print(f"""{Fore.RED}
    
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

███████╗███████╗███╗   ██╗████████╗██╗███╗   ██╗███████╗██╗     ██╗     ███████╗    
██╔════╝██╔════╝████╗  ██║╚══██╔══╝██║████╗  ██║██╔════╝██║     ██║     ██╔════╝    
███████╗█████╗  ██╔██╗ ██║   ██║   ██║██╔██╗ ██║█████╗  ██║     ██║     █████╗      
╚════██║██╔══╝  ██║╚██╗██║   ██║   ██║██║╚██╗██║██╔══╝  ██║     ██║     ██╔══╝      
███████║███████╗██║ ╚████║   ██║   ██║██║ ╚████║███████╗███████╗███████╗███████╗    
╚══════╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝╚══════╝╚══════╝    
                                                                                    
                                                                                                                                                                                                                               Author:  Sentinelle
               Version: v1.0
""")
    options = [
        "1. IP-Lookup",
        "2. Port-Scanner",
        "3. Token Finder",
        "4. Nitro-Gen",
        "5. Web Scanner Advanced",
        "6. Avanced Ip Scanner",
        "7. Username Search (OSINT)"
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
            web()
            again = input("\nVoulez-vous retourner au menu ? (o/n) : ")
            if again.lower() != 'o':
                print("Au revoir!")
                break
        elif choice == '6':
            clear_screen()
            rustscan_scan()
            again = input("\nVoulez-vous retourner au menu ? (o/n) : ")
            if again.lower() != 'o':
                print("Au revoir!")
                break
        elif choice == '7':
            clear_screen()
