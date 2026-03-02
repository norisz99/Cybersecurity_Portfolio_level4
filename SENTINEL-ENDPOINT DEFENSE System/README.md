# 🛡️ SENTINEL - Endpoint Defense System

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square)
![Module](https://img.shields.io/badge/Module-Watchdog-green?style=flat-square)
![Category](https://img.shields.io/badge/Category-EDR_Simulation-blue?style=flat-square)

## 📌 Áttekintés (Overview)
A **SENTINEL** egy könnyűsúlyú **Endpoint Detection and Response (EDR)** keretrendszer prototípusa. A célja, hogy demonstrálja, hogyan működnek a modern végpontvédelmi szoftverek a háttérben. A rendszer nem csak passzívan figyel, hanem aktív csapdákat (**Honeytokens**) állít a támadóknak.

## 🛠️ Funkciók
* **🍯 Honeytoken Trap:** Egy hamis jelszófájlt (`backup_passwords_2005.txt`) helyez el csaliként. Ha bármilyen folyamat megpróbálja olvasni, módosítani vagy törölni, a Sentinel azonnal riaszt.
* **👁️ Real-time Monitoring:** A fájlrendszeri események valós idejű figyelése a `watchdog` könyvtár segítségével.
* **📝 Intrusion Logging:** Minden gyanús tevékenységet naplóz a `sentinel_logs.txt` fájlba, rögzítve az időpontot és az esemény típusát.
* **🔔 Alert System:** Azonnali konzolüzenet (és potenciálisan email riasztás) behatolás észlelésekor.

## ⚙️ Technikai Részletek
* **Nyelv:** Python 3.x
* **Könyvtár:** `watchdog`, `logging`, `time`
* **Mechanizmus:** File System Event Monitoring (Fájlrendszer eseményfigyelés)

## 🚀 Telepítés és Használat

**1. Függőségek telepítése:**
A script a `watchdog` modult használja a fájlrendszer figyelésére.
```bash
pip install watchdog
