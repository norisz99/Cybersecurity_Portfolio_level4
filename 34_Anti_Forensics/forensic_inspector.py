import os
import sys
import time
import datetime
import stat

def get_file_metadata(filepath):
    """
    Részletes metaadat-elemzés a fájlról.
    Ez az eszköz segít megérteni, mit látnak a nyomozók.
    """
    if not os.path.exists(filepath):
        print(f"[-] HIBA: A fájl nem található: {filepath}")
        return

    print(f"\n--- [ FORENSIC ARTIFACT ANALYSIS ] ---")
    print(f"Fájl: {os.path.basename(filepath)}")
    print(f"Teljes útvonal: {os.path.abspath(filepath)}")
    
    # Alapvető statisztikák lekérése
    file_stat = os.stat(filepath)
    
    # 1. Méret elemzés
    print(f"\n[+] Méret: {file_stat.st_size} bájt")
    
    # 2. Időbélyegek (MAC Times - Modified, Accessed, Created)
    # A forensic elemzők ezek inkonzisztenciáját keresik!
    
    # Létrehozás ideje (Creation Time)
    c_time = datetime.datetime.fromtimestamp(file_stat.st_ctime)
    # Módosítás ideje (Last Write / Modification Time)
    m_time = datetime.datetime.fromtimestamp(file_stat.st_mtime)
    # Utolsó hozzáférés (Last Access Time)
    a_time = datetime.datetime.fromtimestamp(file_stat.st_atime)
    
    print("\n[+] Időbélyegek (MAC Times):")
    print(f"    CREATED (Létrehozva):  {c_time}  <-- Mikor került a lemezre?")
    print(f"    MODIFIED (Módosítva):  {m_time}  <-- Mikor írtak bele utoljára?")
    print(f"    ACCESSED (Megnyitva):  {a_time}  <-- Mikor olvasták utoljára?")

    # 3. Anomália detektálás (Logikai ellenőrzés)
    print("\n[?] Elemzés:")
    if m_time > c_time:
        print("    [INFO] A fájlt a létrehozása után módosították (Normális).")
    elif m_time < c_time:
        print("    [!!!] GYANÚS: A módosítási dátum régebbi, mint a létrehozás!")
        print("          Ez gyakori jele a fájl másolásának vagy a Timestomping-nak.")
    
    if abs((a_time - m_time).total_seconds()) < 1:
        print("    [INFO] A módosítás és hozzáférés ideje megegyezik (Friss írás).")

def main():
    os.system("cls" if os.name == 'nt' else "clear")
    print("Forensic Metadata Inspector v1.0")
    print("Használat: Húzz rá egy fájlt a scriptre, vagy írd be az útvonalát.\n")
    
    if len(sys.argv) > 1:
        target_file = sys.argv[1]
    else:
        # Ha nincs argumentum, bekérjük
        target_file = input("Add meg a vizsgálandó fájl útvonalát: ").strip().strip('"')
    
    get_file_metadata(target_file)
    
    input("\nNyomj Entert a kilépéshez...")

if __name__ == "__main__":
    main()