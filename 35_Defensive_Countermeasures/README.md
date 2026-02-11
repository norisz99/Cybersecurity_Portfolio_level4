# 🛡️ Project 35: Windows Defensive Countermeasures

**Focus:** Blue Team, Endpoint Detection & Response (EDR), Registry Monitoring, Honeytokens, File Integrity Monitoring (FIM)

---

## 📌 Overview
Ez a projekt a **Level 4** támadó eszközeinek (Persistence, Credential Dumping) ellenszere. A cél demonstrálni, hogyan detektálhatóak a Windows rendszereken végrehajtott behatolások valós időben, Python alapú megfigyelő eszközökkel.

A modul két védelmi koncepciót valósít meg:
1.  **Registry Sentry:** A rendszerautomatizmusok (Persistence) figyelése.
2.  **Honeytoken Trap:** A bizalmas adatokhoz való illetéktelen hozzáférés (Data Exfiltration) detektálása.

## 🛠 Tools

### 1. Registry Sentry (`registry_sentry.py`)
Ez a script egy EDR (Endpoint Detection and Response) ágens egyszerűsített modellje.
* **Működés:** Másodpercenként ellenőrzi a `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` kulcsot.
* **Detektálás:** Összehasonlítja a jelenlegi állapotot egy bázisállapottal (Baseline). Ha új bejegyzést talál (pl. a *Project 30* malware-ét), azonnal riasztást küld.
* **Használat:** Folyamatosan fut a háttérben.

### 2. Honeyfile Monitor (`honeyfile_monitor.py`)
Ez a script a "Deception Technology" (Megtévesztéses Védelem) elvét alkalmazza.
* **Működés:** Létrehoz egy csali fájlt (`secret_passwords.txt`), amely vonzó célpont a támadók számára.
* **Detektálás:** Figyeli a fájl "Last Access Time" (Utolsó hozzáférés) metaadatát.
* **Riasztás:** Ha a *Project 33* (vagy egy hacker) megpróbálja elolvasni a fájlt, a script azonnal jelzi a behatolást.

## ⚔️ Red vs. Blue Simulation
Hogyan teszteljük a védelmet?

1.  **A Védő indítása:** Indítsd el a `registry_sentry.py`-t egy terminálban.
2.  **A Támadó indítása:** Egy másik terminálban futtasd a `../30_Persistence_Mechanisms/persistence_toolkit.py`-t.
3.  **Eredmény:** A Védő scriptnek azonnal észlelnie kell az új Registry bejegyzést, és felugró ablakkal jeleznie a blokkolást/riasztást.

---

## ⚠️ Jogi Nyilatkozat (Disclaimer)
A kódok oktatási célokat szolgálnak, bemutatva a kiberbiztonsági védekezés alapelveit.