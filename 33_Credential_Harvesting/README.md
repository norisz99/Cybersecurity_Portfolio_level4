# ⚠️ LEGAL DISCLAIMER

**HU:** Ez az eszköz kizárólag **saját rendszerek tesztelésére** vagy a tulajdonos írásos engedélyével rendelkező hálózatokon használható. A szoftver oktatási céllal készült. A szerző (Paczok Norisz) elhárít minden felelősséget a jogellenes használatért vagy károkért.

**EN:** This tool is for **educational purposes and authorized testing only**. The creator (Paczok Norisz) assumes no liability for misuse or any damage caused by this program.

---

# 🦊 Project 33: Browser Credential Harvester

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square)
![Library](https://img.shields.io/badge/Lib-SQLite3%2FCryptography-red?style=flat-square)
![Category](https://img.shields.io/badge/Category-Credential_Theft-red?style=flat-square)

## 📌 Áttekintés (Overview)
Ez az eszköz a böngészőkben (itt: Google Chrome) tárolt jelszavak és cookie-k kinyerésének módját demonstrálja. Megmutatja, hogyan férhet hozzá egy támadó a `Login Data` adatbázishoz, és hogyan fejti vissza a Windows DPAPI (Data Protection API) által védett titkosító kulcsot.

## 🛠️ Funkciók
* **🔓 DPAPI Decryption:** A Windows mesterkulcsának visszafejtése (`Local State` fájlból).
* **🗄️ SQL Extraction:** Jelszavak és felhasználónevek kinyerése a Chrome SQLite adatbázisából.
* **🍪 Cookie Theft:** Munkamenet-sütik (Session Cookies) exportálása.

## ⚙️ Technikai Részletek
* **Nyelv:** Python 3.x
* **Függőségek:** `pywin32`, `cryptography`
* **Cél:** Windows DPAPI rendszer és Chrome Local Storage.

## 🚀 Használat
```bash
python chrome_thief.py
