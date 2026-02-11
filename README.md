# 🛡️ Cybersecurity & Python Portfolio - Level 4

**Author:** [Paczok Norisz]  
**Focus:** Post-Exploitation, Persistence, Privilege Escalation, Anti-Forensics, Defense Evasion

---

## 📌 Overview

Ez a repozitórium a kiberbiztonsági portfólió **negyedik szintje**. Míg az előző szintek a bejutásra fókuszáltak, itt a hangsúly a **rendszerben maradáson (Persistence)** és a **nyomok eltüntetésén (Evasion)** van.

A gyűjtemény olyan haladó technikákat demonstrál, mint a jogosultság-eszkaláció, a vírusirtók megkerülése (Obfuscation), és a digitális nyomozás elleni védekezés, valamint tartalmaz egy integrált védelmi rendszert (SENTINEL) is.

---

## 📂 Project Catalog

### ⚔️ Offensive Tactics & Post-Exploitation

| Project | Description | Key Skills |
| :--- | :--- | :--- |
| **[30_Persistence_Mechanisms](./30_Persistence_Mechanisms)** | Különböző technikák a rendszerhez való tartós hozzáférés biztosítására (Registry kulcsok, Scheduled Taskok, Startup folder). | `winreg`, `subprocess`, Persistence Strategies |
| **[31_Privilege_Escalation](./31_Privilege_Escalation)** | Jogosultságok emelése felhasználói szintről adminisztrátori szintre (pl. UAC Bypass, Token Manipulation szimuláció). | `ctypes`, `pywin32`, Windows API |
| **[32_Obfuscation_Evasion](./32_Obfuscation_Evasion)** | Kódok rejtjelezése és "csomagolása" a statikus analízis és vírusirtók megkerülésére (Payload Encoding, Polymorphism). | `base64`, `xor`, Code Packing |
| **[33_Credential_Harvesting](./33_Credential_Harvesting)** | Jelszavak és hitelesítő adatok kinyerése böngészőkből, Wi-Fi profilokból vagy memóriából (LSASS szimuláció). | `sqlite3`, `json`, Cryptography |
| **[34_Anti_Forensics](./34_Anti_Forensics)** | Nyomok eltüntetése: Eseménynaplók (Event Logs) törlése, fájlok időbélyegének manipulálása (Timestomping) és biztonságos törlés. | `os`, `shutil`, `ctypes` (WinAPI) |

### 🛡️ Defensive Mechanisms

| Project | Description | Key Skills |
| :--- | :--- | :--- |
| **[35_Defensive_Countermeasures](./35_Defensive_Countermeasures)** | Kék csapat (Blue Team) eszközök, amelyek detektálják a fenti támadási kísérleteket és riasztást küldenek. | `logging`, Pattern Matching, System Monitoring |
| **[SENTINEL-ENDPOINT DEFENSE System](./SENTINEL-ENDPOINT DEFENSE System)** | **Capstone Module:** Egy átfogó végpontvédelmi keretrendszer, amely egyesíti a detektálást, a naplózást és a valós idejű reagálást. | `multiprocessing`, Real-time Analysis, SIEM Logic |

---

## 🛠 Technologies Used

* **Language:** Python 3.10+
* **System Interaction:** `os`, `sys`, `subprocess`, `winreg`
* **Windows API:** `ctypes`, `pywin32`
* **Obfuscation:** `base64`, Custom XOR algorithms
* **Environment:** Windows 10/11 Target Machines, VS Code

---

## ⚠️ Jogi Nyilatkozat (Disclaimer)

A repozitóriumban található kódok kizárólag **oktatási és etikus kiberbiztonsági kutatási** célokat szolgálnak. A szoftverek bármilyen engedély nélküli, rosszindulatú használata illegális és súlyos jogi következményeket vonhat maga után. A készítő nem vállal felelősséget a kódok nem rendeltetésszerű használatáért.
