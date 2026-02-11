# 🔓 Project 31: Privilege Escalation (UAC Bypass)

**Focus:** User Account Control (UAC), Registry Manipulation, Fodhelper Technique, Admin Rights

---

## 📌 Overview
Ez a modul a **Privilege Escalation** (Jogosultság Kiterjesztés) egyik legismertebb technikáját, a "Fodhelper Bypass"-t demonstrálja. A cél a rendszergazdai (High Integrity) jogosultság megszerzése anélkül, hogy a felhasználónak megjelenne a figyelmeztető UAC ("Engedélyezi-e...") ablak.

A script kihasználja a Windows `fodhelper.exe` (Features on Demand Helper) binárisának automatikus jogemelési tulajdonságát és a Registry-ből történő parancsvégrehajtási sérülékenységét.

## ⚙️ Features
* **Silent Elevation:** A script adminisztrátori jogokkal indul újra felhasználói beavatkozás nélkül.
* **Registry Injection:** A `HKCU\Software\Classes\ms-settings\Shell\Open\command` kulcs manipulálása.
* **Proof of Concept:** Sikeres támadás esetén a script létrehoz egy bizonyíték fájlt (`norisz_proof.txt`) a védett `C:\Windows` rendszerkönyvtárban, ahová csak Adminisztrátorok írhatnak.
* **Auto-Cleanup:** A támadás után a script törli a Registry bejegyzéseket a nyomok eltüntetése érdekében.

## 🛠 Usage
Windows környezetben futtatandó.

1. **Indítás:**
   ```bash
   python uac_bypass.py