import os
import time
import ctypes

# A csali fájl neve - Legyen valami, amiért a hacker lehajol!
HONEY_FILE = "backup_passwords_2005.txt"

def create_honeyfile():
    """Létrehozza a csalit hitelesnek tűnő, de FAKE adatokkal."""
    
    # Ez a tartalom úgy néz ki, mint egy régi SQL dump vagy ellopott lista
    fake_content = """
# EXPORT DATE: 2005-11-04
# SERVER: WIN-SRV-2003
# DB: USERS_LEGACY

admin@hotmail.com:admin123
root@yahoo.com:toor
skater_boi88@aol.com:blink182
dark_angel@msn.com:matrix
princess_sophie@hotmail.com:iloveyou
webmaster@freemail.hu:password
matrix_neo@yahoo.com:trinity
dragon_slayer@aol.com:qwerty
coolguy_nyc@hotmail.com:123456
system_backup@internal.local:S3cr3t!
john.doe@corp.net:mustang
mary.smith@corp.net:sunshine
test_user@yahoo.com:test
game_master@msn.com:wow123
linkin_park_fan@hotmail.com:numb
super_admin@localhost:godmode
"""

    if not os.path.exists(HONEY_FILE):
        with open(HONEY_FILE, "w", encoding="utf-8") as f:
            f.write(fake_content.strip())
        
        print(f"[+] Csali fájl létrehozva: {os.path.abspath(HONEY_FILE)}")
        print("[+] Tartalom: 2000-es évek stílusú jelszólista (Fake Data).")
        
        # Opcionális: Rejtetté tehetjük, de egy hacker úgyis látja a rejtett fájlokat
        # os.system(f"attrib +h {HONEY_FILE}") 

def get_file_access_time():
    """Lekérdezi, mikor nyúltak hozzá utoljára a fájlhoz."""
    return os.path.getatime(HONEY_FILE)

def main():
    os.system("cls")
    print("--- [ BLUE TEAM: HONEYFILE MONITOR v2.0 ] ---")
    print("       (Historical Data Simulation)          ")
    
    create_honeyfile()
    
    print("\n[*] A csapda élesítve.")
    print(f"[*] Figyelt fájl: {HONEY_FILE}")
    print("[*] Várakozás a behatolóra...")
    
    try:
        # Kezdő időpont
        last_access = get_file_access_time()
        
        while True:
            current_access = get_file_access_time()
            
            # Ha az utolsó hozzáférés ideje megváltozott...
            if current_access != last_access:
                timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(current_access))
                print(f"\n[!!!] RIASZTÁS ({timestamp}): HOZZÁFÉRÉS ÉSZLELVE!")
                print(f"      Valaki megnyitotta a '{HONEY_FILE}' fájlt!")
                
                # Felugró ablak
                ctypes.windll.user32.MessageBoxW(0, 
                    f"Behatolás észlelve!\nA {HONEY_FILE} fájlt megnyitották.", 
                    "Honeyfile Alert - SECURITY BREACH", 0x10)
                
                # Frissítjük, hogy újra riaszthasson
                last_access = current_access
            
            time.sleep(1) # CPU kímélő mód
            
    except KeyboardInterrupt:
        print("\n[*] Leállítás...")
        # Takarítás: Töröljük a csalit a kilépéskor
        if os.path.exists(HONEY_FILE):
            os.remove(HONEY_FILE)
            print("[*] Csali fájl törölve.")

if __name__ == "__main__":
    main()