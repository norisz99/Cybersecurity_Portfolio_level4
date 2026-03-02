# ⚠️ LEGAL DISCLAIMER

**HU:** Ez az eszköz kizárólag **saját rendszerek tesztelésére** vagy a tulajdonos írásos engedélyével rendelkező hálózatokon használható. A szoftver oktatási céllal készült. A szerző (Paczok Norisz) elhárít minden felelősséget a jogellenes használatért vagy károkért.

**EN:** This tool is for **educational purposes and authorized testing only**. The creator (Paczok Norisz) assumes no liability for misuse or any damage caused by this program.

---

# 🧛 Project 30: Persistence Mechanisms Toolkit

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square)
![Library](https://img.shields.io/badge/Lib-WinReg-yellow?style=flat-square)
![Category](https://img.shields.io/badge/Category-APT_Simulation-red?style=flat-square)

## 📌 Áttekintés (Overview)
Ez a projekt a **Perzisztencia (Persistence)** technikáit demonstrálja Windows környezetben. A kiberbiztonságban ez a fázis biztosítja, hogy a bejutás után a hozzáférés akkor is megmaradjon, ha a felhasználó újraindítja a gépet vagy kijelentkezik.

## 🛠️ Funkciók
* **🗝️ Registry Manipulation:** Automatikus indítókulcs (`Run` key) létrehozása a Windows Registry-ben.
* **📅 Scheduled Tasks:** Időzített feladatok létrehozása a háttérben (a leggyakoribb malware technika).
* **🕵️ Stealth Mode:** A perzisztencia elrejtése a feladatkezelő elől (szimuláció).

## ⚙️ Technikai Részletek
* **Nyelv:** Python 3.x
* **Könyvtárak:** `winreg` (Registry hozzáférés), `os` (Parancssori utasítások)
* **Célpont:** Windows OS (Registry & Task Scheduler)

## 🚀 Használat
```bash
python persistence_toolkit.py
