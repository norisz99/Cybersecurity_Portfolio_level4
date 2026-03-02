# ⚠️ LEGAL DISCLAIMER

**HU:** Ez az eszköz kizárólag **saját rendszerek tesztelésére** vagy a tulajdonos írásos engedélyével rendelkező hálózatokon használható. A szoftver oktatási céllal készült. A szerző (Paczok Norisz) elhárít minden felelősséget a jogellenes használatért vagy károkért.

**EN:** This tool is for **educational purposes and authorized testing only**. The creator (Paczok Norisz) assumes no liability for misuse or any damage caused by this program.

---

# 🕰️ Project 34: Anti-Forensics Toolkit (Timestomping)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square)
![Technique](https://img.shields.io/badge/Technique-Timestomping-orange?style=flat-square)
![Category](https://img.shields.io/badge/Category-Anti_Forensics-red?style=flat-square)

## 📌 Áttekintés (Overview)
Ez a projekt az **Anti-Forensics** (Digitális nyomrögzítés elleni) technikákat mutatja be, különös tekintettel a **Timestomping**-ra. A program képes manipulálni a fájlok metaadatait (létrehozás, módosítás, hozzáférés dátuma), hogy elrejtse a fájl valódi eredetét a forenzikus vizsgálat elől.

## 🛠️ Funkciók
* **📅 Timestamp Manipulation:** Fájlok időbélyegeinek tetszőleges átírása.
* **🕵️ Metadata Spoofing:** A "támadó" fájlok elrejtése úgy, mintha régi rendszerfájlok lennének.
* **🔍 Forensic Inspection:** A fájlok valódi és módosított dátumainak elemzése.

## ⚙️ Technikai Részletek
* **Nyelv:** Python 3.x
* **API:** `os.utime`, `pywin32` (SetFileTime)
* **Cél:** A `MACE` (Modified, Accessed, Created, Entry) attribútumok hamisítása.

## 🚀 Használat
```bash
python timestomper.py --target "malware.exe" --date "2020-01-01 10:00:00"
