# ⚠️ LEGAL DISCLAIMER

**HU:** Ez az eszköz kizárólag **saját rendszerek tesztelésére** vagy a tulajdonos írásos engedélyével rendelkező hálózatokon használható. A szoftver oktatási céllal készült. A szerző (Paczok Norisz) elhárít minden felelősséget a jogellenes használatért vagy károkért.

**EN:** This tool is for **educational purposes and authorized testing only**. The creator (Paczok Norisz) assumes no liability for misuse or any damage caused by this program.

---

# 👑 Project 31: UAC Bypass (Privilege Escalation)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square)
![Technique](https://img.shields.io/badge/Technique-Registry_Hijacking-red?style=flat-square)
![Category](https://img.shields.io/badge/Category-PrivEsc-red?style=flat-square)

## 📌 Áttekintés (Overview)
Ez az eszköz a **Privilege Escalation** (Jogosultság-emelés) egyik legismertebb formáját, a **UAC (User Account Control) Bypass** technikát mutatja be. A program kihasználja a Windows `fodhelper.exe` megbízható folyamatának sérülékenységét, hogy rendszergazdai jogokkal futtasson parancsokat a felhasználó jóváhagyása nélkül.

## 🛠️ Funkciók
* **🔓 Silent Elevation:** Rendszergazdai jogok szerzése felugró ablak (prompt) nélkül.
* **📂 Registry Hijacking:** A `HKCU\Software\Classes\ms-settings\Shell\Open\command` kulcs manipulálása.
* **🚀 Fodhelper Exploit:** A Windows beépített eszközének felhasználása a támadáshoz (Living off the Land).

## ⚙️ Technikai Részletek
* **Nyelv:** Python 3.x
* **Módszer:** Fileless UAC Bypass (Registry alapú)
* **Veszélyességi szint:** Magas (High Integrity Level szerzése)

## 🚀 Használat
```bash
python uac_bypass.py
