# 🔑 Project 33: Multi-Browser Credential Harvester

**Focus:** Post-Exploitation, DPAPI (Data Protection API), AES Encryption, SQLite, Forensic Data Recovery

---

## 📌 Overview
Ez a projekt egy fejlett **Credential Dumping** (Hitelesítőadat-kinyerő) eszközt valósít meg, amely képes a legnépszerűbb Chromium-alapú böngészőkből (Google Chrome, Microsoft Edge, Opera, Opera GX) kinyerni a mentett belépési adatokat.

A modern böngészők a jelszavakat egy helyi SQLite adatbázisban tárolják, AES-256-GCM titkosítással védve. A kulcsot a Windows DPAPI (Data Protection API) védi. Mivel a script a felhasználó jogosultságaival fut, képes feloldani ezt a védelmet és visszafejteni az adatbázist.

## ⚙️ Features
* **Multi-Browser Support:** Automatikus detektálás és kinyerés a következőkhöz: Chrome, Edge, Opera Stable, Opera GX.
* **Master Key Extraction:** A `Local State` fájl feldolgozása és a DPAPI titkosított kulcs megszerzése.
* **AES Decryption:** A jelszavak visszafejtése a `pycryptodome` könyvtár segítségével.
* **Smart Filtering:** Több felhasználói profil (Default, Profile 1, Profile 2) párhuzamos kezelése.
* **Loot Saving:** A kinyert adatokat nemcsak megjeleníti, hanem egy strukturált szöveges fájlba (`megszerzett_jelszavak.txt`) is menti.

## 🛠 Usage
A scriptet a célpont gépén kell futtatni (Python környezet szükséges).

1. **Függőségek telepítése:**
   ```bash
   pip install pycryptodome pypiwin32