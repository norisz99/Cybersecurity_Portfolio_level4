# 🛡️ Project 35: Defensive Countermeasures (Honeypots)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square)
![Technique](https://img.shields.io/badge/Technique-Deception-green?style=flat-square)
![Category](https://img.shields.io/badge/Category-Blue_Team-blue?style=flat-square)

## 📌 Áttekintés (Overview)
Ez a projekt a **Deception Technology** (Megtévesztéses Védelem) alapjait mutatja be. Olyan csapdákat (Honeyfile, Registry Sentry) hoz létre, amelyek riasztják a védőket, ha egy támadó vagy zsarolóvírus megpróbálja módosítani őket.

## 🛠️ Funkciók
* **🍯 Honeyfile Monitor:** Hamis fájlokat ("csali dokumentumokat") helyez el, és figyeli a hozzáféréseket. Ha valaki megnyitja, az riasztást generál.
* **🛡️ Registry Sentry:** Védi a kritikus rendszerkulcsokat (pl. AutoRun), és azonnal jelez, ha egy malware perzisztenciát próbál beállítani.
* **🔔 Real-time Alerting:** Azonnali visszajelzés a behatolási kísérletekről.

## ⚙️ Technikai Részletek
* **Nyelv:** Python 3.x
* **API:** `watchdog` (File monitoring), `winreg` (Registry monitoring)
* **Felhasználás:** Korai detektálás (Early Warning System).

## 🚀 Használat
```bash
python honeyfile_monitor.py
