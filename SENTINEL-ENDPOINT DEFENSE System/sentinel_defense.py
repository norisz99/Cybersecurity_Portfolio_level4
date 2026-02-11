import os
import time
import sys
import threading
import ctypes
import winreg as reg
from datetime import datetime

# --- KONFIGURÁCIÓ ---
LOG_FILE = "sentinel_logs.txt"
HONEY_FILE = "backup_passwords_2005.txt"
REG_PATH = r"Software\Microsoft\Windows\CurrentVersion\Run"

# --- SEGÉDFÜGGVÉNYEK ---
def log_event(level, message):
    """Központi naplózó rendszer: Képernyőre és Fájlba is ír."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_msg = f"[{timestamp}] [{level}] {message}"
    
    # Képernyőre
    print(formatted_msg)
    
    # Fájlba
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(formatted_msg + "\n")

def show_alert_box(title, message):
    """Felugró Windows ablak a kritikus hibáknál."""
    ctypes.windll.user32.MessageBoxW(0, message, title, 0x10 | 0x1000)

def startup_sequence():
    """A 'Csillog-Villog' effekt: Rendszerbetöltés szimuláció."""
    os.system("cls")
    os.system("color 0A") # Mátrix zöld
    
    ascii_art = """
    ███████╗███████╗███╗   ██╗████████╗██╗███╗   ██╗███████╗██╗     
    ██╔════╝██╔════╝████╗  ██║╚══██╔══╝██║████╗  ██║██╔════╝██║     
    ███████╗█████╗  ██╔██╗ ██║   ██║   ██║██╔██╗ ██║█████╗  ██║     
    ╚════██║██╔══╝  ██║╚██╗██║   ██║   ██║██║╚██╗██║██╔══╝  ██║     
    ███████║███████╗██║ ╚████║   ██║   ██║██║ ╚████║███████╗███████╗
    ╚══════╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝
    --- ENDPOINT DEFENSE SYSTEM v1.0 ---
    """
    print(ascii_art)
    print("Initializing Core Modules...")
    modules = [
        "Loading Kernel Drivers...",
        "Connecting to Registry API...",
        "Mounting File System Watchdogs...",
        "Encrypting Log Channels...",
        "SENTINEL ACTIVE."
    ]
    for mod in modules:
        time.sleep(0.8) # Kis várakozás a drámai hatásért
        print(f"[OK] {mod}")
    print("-" * 60)
    print("SYSTEM MONITORING STARTED. PRESS CTRL+C TO HALT.")
    print("-" * 60)

# --- MODULE 1: REGISTRY MONITOR ---
def registry_watchdog():
    log_event("INFO", "Registry Watchdog thread started.")
    
    # Bázisállapot felvétele
    baseline = {}
    try:
        key = reg.OpenKey(reg.HKEY_CURRENT_USER, REG_PATH, 0, reg.KEY_READ)
        i = 0
        while True:
            try:
                name, value, _ = reg.EnumValue(key, i)
                baseline[name] = value
                i += 1
            except OSError:
                break
        reg.CloseKey(key)
    except Exception as e:
        log_event("ERROR", f"Registry init failed: {e}")
        return

    while True:
        try:
            current_values = {}
            key = reg.OpenKey(reg.HKEY_CURRENT_USER, REG_PATH, 0, reg.KEY_READ)
            i = 0
            while True:
                try:
                    name, value, _ = reg.EnumValue(key, i)
                    current_values[name] = value
                    i += 1
                except OSError:
                    break
            reg.CloseKey(key)
            
            # Összehasonlítás
            for name, value in current_values.items():
                if name not in baseline:
                    log_event("CRITICAL", f"REGISTRY ATTACK DETECTED! Key: {name} | Cmd: {value}")
                    show_alert_box("SENTINEL ALERT", f"Illetéktelen módosítás az automatikus indításban!\n{name}")
                    baseline = current_values # Frissítjük, hogy ne floodoljon
            
            time.sleep(2)
        except Exception as e:
            log_event("ERROR", f"Registry loop error: {e}")

# --- MODULE 2: HONEYFILE MONITOR ---
def honeyfile_watchdog():
    log_event("INFO", "Honeytoken Watchdog thread started.")
    
    # 1. Létrehozzuk a csalit, ha nincs
    if not os.path.exists(HONEY_FILE):
        content = """
# EXPORT 2005 - DO NOT SHARE
admin@hotmail.com:12345
root@yahoo.com:toor
"""
        with open(HONEY_FILE, "w") as f:
            f.write(content)
        log_event("INFO", f"Honeytoken generated: {HONEY_FILE}")

    last_access = os.path.getatime(HONEY_FILE)

    while True:
        try:
            current_access = os.path.getatime(HONEY_FILE)
            if current_access != last_access:
                log_event("CRITICAL", f"HONEYTOKEN BREACHED! File accessed: {HONEY_FILE}")
                show_alert_box("SENTINEL ALERT", f"Adatszivárgási kísérlet!\nA csali fájlt megnyitották.")
                last_access = current_access
            
            time.sleep(1)
        except Exception as e:
            log_event("ERROR", f"Honeytoken loop error: {e}")

# --- MAIN CONTROLLER ---
def main():
    startup_sequence()
    
    # Szálak (Threads) indítása
    # Ez teszi lehetővé, hogy a két védelem PÁRHUZAMOSAN fusson
    t1 = threading.Thread(target=registry_watchdog, daemon=True)
    t2 = threading.Thread(target=honeyfile_watchdog, daemon=True)
    
    t1.start()
    t2.start()
    
    try:
        # A fő szál csak várakozik, amíg a "gyerekek" dolgoznak
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n" + "-" * 60)
        log_event("INFO", "System shutdown initiated by user.")
        print("-" * 60)

if __name__ == "__main__":
    main()