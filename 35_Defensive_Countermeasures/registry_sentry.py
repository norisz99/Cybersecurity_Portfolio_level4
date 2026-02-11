import winreg as reg
import time
import os
import ctypes
from datetime import datetime

# A kulcs, amit figyelünk (Ugyanaz, amit a Project 30 támadott)
REG_PATH = r"Software\Microsoft\Windows\CurrentVersion\Run"

def get_registry_values():
    """Lekérdezi az összes jelenlegi értéket a Run kulcsból."""
    values = {}
    try:
        key = reg.OpenKey(reg.HKEY_CURRENT_USER, REG_PATH, 0, reg.KEY_READ)
        i = 0
        while True:
            try:
                # Név és Érték (pl. "UpdateManager", "C:\virus.py")
                name, value, _ = reg.EnumValue(key, i)
                values[name] = value
                i += 1
            except OSError:
                break
        reg.CloseKey(key)
    except Exception as e:
        print(f"[!] Hiba a Registry olvasásakor: {e}")
    return values

def alert_user(name, value):
    """RIASZTÁS! Felugró ablak és hangjelzés."""
    print(f"\n[!!!] RIASZTÁS: Új automatikus indítás észlelve!")
    print(f"      Név: {name}")
    print(f"      Parancs: {value}")
    
    # Windows hibaüzenet ablak
    ctypes.windll.user32.MessageBoxW(0, 
        f"Gyanús aktivitás észlelve!\n\nÚj elem a Registry-ben:\n{name}\n{value}", 
        "Registry Sentry - RIASZTÁS", 
        0x10 | 0x1000) # Ikon: Stop, System Modal (előtérbe hozza)

def main():
    os.system("cls")
    print("--- [ BLUE TEAM: REGISTRY SENTRY ] ---")
    print("[*] Védelmi rendszer indítása...")
    print(f"[*] Figyelt útvonal: HKCU\\{REG_PATH}")
    
    # 1. Alapállapot felvétele (Baseline)
    # Megjegyezzük, mi volt ott az induláskor (a "jó" állapot)
    baseline = get_registry_values()
    print(f"[OK] Bázisállapot rögzítve. ({len(baseline)} elem)")
    print("[*] Figyelés aktív. (Nyomj Ctrl+C-t a leállításhoz)")

    try:
        while True:
            # 2. Jelenlegi állapot lekérdezése
            current_state = get_registry_values()
            
            # 3. Összehasonlítás: Van-e olyan kulcs MOST, ami a Bázisban NEM volt?
            for name, value in current_state.items():
                if name not in baseline:
                    # BINGO! Valaki beírta magát.
                    alert_user(name, value)
                    
                    # Frissítjük a bázist, hogy ne riasszon folyamatosan ugyanarra
                    baseline = current_state
            
            # Ellenőrizhetnénk törlést is, de most a hozzáadás a kritikus
            
            time.sleep(2) # 2 másodpercenként ellenőriz
            
    except KeyboardInterrupt:
        print("\n[*] Leállítás...")

if __name__ == "__main__":
    main()