import requests
import whois
import socket
import nmap

def get_website_info(url):
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

        # Whois lookup
        domain = url.split("//")[-1].split("/")[0]  # Extraire le domaine
        whois_info = whois.whois(domain)  # Appel à whois sur le domaine
        print("\nInformations WHOIS :")
        print(f"Propriétaire : {whois_info.owner or 'Inconnu'}")
        print(f"Email : {whois_info.emails or 'Inconnu'}")
        print(f"Créé le : {whois_info.creation_date or 'Inconnu'}")
        print(f"Expire le : {whois_info.expiration_date or 'Inconnu'}")

        # Recherche des vulnérabilités
        check_vulnerabilities(server_info)

        # Scanner Nmap
        nmap_scan(ip_address)

    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de l'accès au site : {e}")
    except Exception as e:
        print(f"Erreur lors de la récupération des informations WHOIS : {e}")

def check_vulnerabilities(server_info):
    # Une simple vérification des vulnérabilités (peut être améliorée)
    known_vulnerabilities = {
        "Apache": "https://www.cvedetails.com/vulnerability-list/vendor_id-45/product_id-1748/Apache-Apache.html",
        "nginx": "https://www.cvedetails.com/vulnerability-list/vendor_id-391/product_id-30720/Nginx-Nginx.html",
        "IIS": "https://www.cvedetails.com/vulnerability-list/vendor_id-40/product_id-41529/Microsoft-IIS.html"
    }

    for server in known_vulnerabilities.keys():
        if server in server_info:
            print(f"\nVulnérabilités connues pour {server} :")
            print(known_vulnerabilities[server])
            return
    
    print("\nAucune vulnérabilité connue pour ce serveur.")

def nmap_scan(ip_address):
    print("\nDémarrage du scan Nmap...")
    nm = nmap.PortScanner()
    nm.scan(ip_address)

    print(f"\nRésultats du scan Nmap pour {ip_address} :")
    print(f"État : {nm[ip_address].state()}")

    for proto in nm[ip_address].all_protocols():
        print(f"\nProtocole : {proto}")
        lport = nm[ip_address][proto].keys()
        for port in sorted(lport):
            print(f"Port : {port}\tÉtat : {nm[ip_address][proto][port]['state']}")

if __name__ == "__main__":
    url = input("Entrez l'URL du site (ex : https://example.com) : ")
    get_website_info(url)

