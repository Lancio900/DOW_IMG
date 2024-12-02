import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def menu():
    print("""
    
        ██╗███╗   ███╗ ██████╗     ███████╗██╗████████╗███████╗
        ██║████╗ ████║██╔════╝     ██╔════╝██║╚══██╔══╝██╔════╝
        ██║██╔████╔██║██║  ███╗    ███████╗██║   ██║   █████╗  
        ██║██║╚██╔╝██║██║   ██║    ╚════██║██║   ██║   ██╔══╝  
        ██║██║ ╚═╝ ██║╚██████╔╝    ███████║██║   ██║   ███████╗
        ╚═╝╚═╝     ╚═╝ ╚═════╝     ╚══════╝╚═╝   ╚═╝   ╚══════╝
                                       
                    Img downloader for site(v0.1)                
                                        	
      """)
    print("")
    print("\n1- Download Image by link (ex. 'background.png' as link)")	
    print("\n2- Download Image by form img")
    print("\n3- Exit")
    
    try:
        s_down = int(input("\nChoose a option: "))
    except ValueError:
        print("[Error] option not found.")
        return

    if s_down == 1:
        download_images_by_link()

    elif s_down == 2:
        download_images_by_form()
    
    elif s_down == 3:
    	print("Come back !")
    	exit()
	
    else:
        print("[!] Option not found.")
        menu()

def download_images_by_link():
    # Chiedi all'utente di inserire l'URL delle immagini
    base_url = input("Enter the link address with the images as links: ")

    # Directory di destinazione per le immagini scaricate
    download_folder = "downloaded_images"

    # Crea la directory di destinazione se non esiste
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    # Invia una richiesta GET alla pagina
    response = requests.get(base_url)
    print(f"Status Code: {response.status_code}")  # Stampa il codice di stato HTTP

    if response.status_code != 200:
        print(f"[Error] Unable to reach the web page {base_url}")
        return

    # Usa BeautifulSoup per analizzare il contenuto HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Trova tutti i link delle immagini (tag <a> con href che puntano a file immagine)
    image_links = []
    for link in soup.find_all('a', href=True):
        img_url = link.get('href')
        
        # Verifica se il link punta ad un'immagine
        if img_url.endswith(('.png', '.jpg', '.jpeg', '.gif', '.svg')):
            # Aggiungi il prefisso per ottenere il percorso completo dell'immagine
            full_img_url = urljoin(base_url, img_url)
            image_links.append(full_img_url)

    # Se non ci sono immagini, stampa un messaggio e esce
    if not image_links:
        print("[INFO] No image found.")
        return

    # Funzione per scaricare le immagini
    def download_image(url, folder_path):
        # Crea il percorso completo per salvare l'immagine
        local_filename = os.path.join(folder_path, os.path.basename(url))
        
        # Controlla se l'immagine è già stata scaricata
        if os.path.exists(local_filename):
            print(f"[INFO] Image {local_filename} already exists. Skipping the download.")
            return
        
        # Invia una richiesta GET per scaricare l'immagine
        print(f"[INFO] Downloading {url}...")
        img_response = requests.get(url, stream=True)
        
        # Verifica se la richiesta è andata a buon fine
        if img_response.status_code == 200:
            with open(local_filename, 'wb') as f:
                for chunk in img_response.iter_content(1024):
                    f.write(chunk)
            print(f"[!] Downloaded image: {local_filename}")
        else:
            print(f"[Error] Error downloading image {url}. Status code: {img_response.status_code}")

    # Scarica tutte le immagini trovate
    for img_url in image_links:
        download_image(img_url, download_folder)

    print("[INFO] All images have been downloaded")
    input("Press Enter: ")
    menu()

def download_images_by_form():
    print("[INFO] Feature still in development")
    menu()

# Avvia il programma
menu()
