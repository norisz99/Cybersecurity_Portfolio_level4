# ⚓ Project 30: Persistence Mechanisms

**Focus:** Post-Exploitation, Windows Registry (winreg), Startup Folder, Python Scripting

---

## 📌 Overview
Ez a projekt egy **Persistence** (Tartósság) eszközt valósít meg, amely demonstrálja, hogyan képes egy program "túlélni" a rendszer újraindítását. A script két klasszikus technikát alkalmaz, hogy felhasználói (User) jogosultsági szinten beépüljön a Windows indítási folyamatába, biztosítva a kód automatikus lefutását minden bejelentkezéskor.

## ⚙️ Features
* **Registry Persistence:** A `winreg` könyvtár segítségével bejegyzést hoz létre a `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` kulcsban.
* **Startup Folder Injection:** A script másolatot készít magáról a felhasználó Indítópult (Startup) mappájába.
* **Stealth (Álcázás):** A Registry-ben és a Startup mappában is ártalmatlan névvel (`SystemUpdate_Check.py`) jelenik meg, hogy elkerülje az átlagos felhasználó gyanúját.
* **Cleanup Mechanism:** Beépített funkció a tesztelés utáni nyomok (Registry kulcsok és fájlok) automatikus eltávolítására.

## 🛠 Usage
A scriptet Windows környezetben (CMD vagy PowerShell) kell futtatni. A program interaktív menüvel rendelkezik.

1. **Futtatás:**
   ```bash
   python persistence_toolkit.py