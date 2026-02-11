import sys
import os
import time
from datetime import datetime
import ctypes
from ctypes import wintypes

# --- Windows API Struktúrák definíciója (ne ijedj meg, ez a "mélyvíz") ---
# Ahhoz, hogy hozzáférjünk a "Creation Time"-hoz, le kell nyúlnunk a kernel szintre.

class FILETIME(ctypes.Structure):
    _fields_ = [("dwLowDateTime", wintypes.DWORD),
                ("dwHighDateTime", wintypes.DWORD)]

# Külső függvények betöltése a Windows kernelből
kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)

CreateFileW = kernel32.CreateFileW
SetFileTime = kernel32.SetFileTime
CloseHandle = kernel32.CloseHandle

def datetime_to_filetime(dt):
    """Átalakítja a Python dátumot Windows FILETIME formátummá (100ns egységek 1601 óta)."""
    EPOCH_AS_FILETIME = 116444736000000000
    HUNDREDS_OF_NANOSECONDS = 10000000
    
    if dt is None:
        return None
    timestamp = dt.timestamp()
    filetime_val = EPOCH_AS_FILETIME + (int(timestamp * HUNDREDS_OF_NANOSECONDS))
    
    ft = FILETIME()
    ft.dwLowDateTime = filetime_val & 0xFFFFFFFF
    ft.dwHighDateTime = filetime_val >> 32
    return ft

def change_file_timestamps(filepath, new_time):
    """
    Ez a függvény végzi a "Timestomping"-ot.
    Átírja a Létrehozás (Creation), Hozzáférés (Access) és Módosítás (Write) idejét is.
    """
    print(f"[*] Célpont: {filepath}")
    print(f"[*] Új dátum beállítása: {new_time}")

    # 1. Fájl megnyitása írási joggal a metaadatokhoz
    GENERIC_WRITE = 0x40000000
    OPEN_EXISTING = 3
    FILE_WRITE_ATTRIBUTES = 0x0100

    handle = CreateFileW(
        filepath,
        FILE_WRITE_ATTRIBUTES, # Csak az attribútumokat akarjuk írni
        0, None,
        OPEN_EXISTING,
        0x02000000, # FILE_FLAG_BACKUP_SEMANTICS (könyvtárakhoz is jó)
        None
    )

    if handle == -1:
        print("[-] HIBA: Nem sikerült megnyitni a fájlt (lehet, hogy használatban van?).")
        return False

    # 2. Az időbélyegek konvertálása
    ft = datetime_to_filetime(new_time)
    
    # 3. A hamisítás végrehajtása (mindhárom időbélyeget ugyanarra állítjuk)
    # Paraméterek: Handle, CreationTime, AccessTime, WriteTime
    success = SetFileTime(handle, ctypes.byref(ft), ctypes.byref(ft), ctypes.byref(ft))
    
    CloseHandle(handle)

    if success:
        print("[+] SIKER! Az időbélyegek átírva.")
        return True
    else:
        print("[-] HIBA: A Windows API visszautasította a kérést.")
        return False

# --- FŐ PROGRAM ---
if __name__ == "__main__":
    os.system("cls")
    print("--- [ LEVEL 4: TIMESTOMPER (Dátum Hamisító) ] ---")
    
    # Bekérjük a fájl nevét
    target = input("Add meg a fájl útvonalát (amit 'megöregítünk'): ").strip().strip('"')
    
    if not os.path.exists(target):
        print("[-] A fájl nem létezik!")
        sys.exit()

    # Bekérjük a hamis dátumot (vagy használunk egy alapértelmezettet)
    date_str = input("Adj meg egy dátumot (YYYY-MM-DD HH:MM) vagy nyomj Entert a [2020-01-01 12:00]-hoz: ")
    
    if date_str.strip() == "":
        fake_date = datetime(2020, 1, 1, 12, 0, 0)
    else:
        try:
            fake_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
        except ValueError:
            print("[-] Rossz formátum! Használd ezt: 2023-05-20 14:30")
            sys.exit()

    change_file_timestamps(target, fake_date)