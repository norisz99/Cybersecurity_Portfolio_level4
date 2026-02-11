# 🔍 Project 34: Anti-Forensics & Timestamp Analysis

**Focus:** Digital Forensics, Metadata Manipulation, Timestomping, Windows API, Defense Evasion

---

## 📌 Overview
Ez a modul a digitális nyomozás (Forensics) és a nyomeltüntetés (Anti-Forensics) macska-egér játékát demonstrálja. A cél bemutatni, hogy a fájlrendszer metaadatai (létrehozás, módosítás ideje) manipulálhatók, és hogy a védelmi oldal hogyan próbálja ezt detektálni.

A projekt két eszközt tartalmaz:
1. **The Inspector (Blue Team):** Egy elemző eszköz, amely kiolvassa a fájlok látható időbélyegeit.
2. **The Timestomper (Red Team):** Egy demonstrációs eszköz, amely a Windows Kernel API (`SetFileTime`) segítségével tetszőleges dátumra írja át a fájlok időbélyegeit.

## ⚙️ Tools

### 1. Forensic Inspector (`forensic_inspector.py`)
Ez a script "röntgen alá teszi" a fájlt.
* **Funkció:** Lekérdezi a MAC (Modified, Accessed, Created) időket.
* **Cél:** Anomáliák keresése (pl. ha a Módosítás dátuma régebbi, mint a Létrehozás dátuma).

### 2. Timestomper (`timestomper.py`)
Ez a script végzi a manipulációt.
* **Technika:** A `kernel32.dll` könyvtáron keresztül közvetlenül hívja meg a Windows API-t.
* **Cél:** A `$Standard_Information` attribútum felülírása az NTFS fájlrendszerben, hogy a fájl réginek és ártatlannak tűnjön a Fájlkezelőben.

## 🛡️ Blue Team / Védekezés
Hogyan lehet lebuktatni a Timestompingot?
* **MFT Elemzés:** A profi forensic eszközök (pl. EnCase, MFTECmd) nemcsak a `$Standard_Information` (könnyen hamisítható), hanem a `$FileName` (nehezen hamisítható) attribútumot is kiolvassák.
* **Time Skew:** Ha a két attribútum között eltérés van (pl. a fájl "látszólag" 2020-as, de a `$FileName` rekord 2024-es), az egyértelmű jele a beavatkozásnak.

## 🛠 Usage

**1. Elemzés (Előtte):**
```bash
python forensic_inspector.py celpont.txt