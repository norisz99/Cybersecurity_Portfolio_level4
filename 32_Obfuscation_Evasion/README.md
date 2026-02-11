# 🎭 Project 32: Obfuscation & Evasion (FUD Payload)

**Focus:** Antivirus Evasion, Cryptography (XOR), Polymorphism, Python Dynamic Execution

---

## 📌 Overview
Ez a projekt egy **Payload Builder** (Kód-generáló) eszközt valósít meg, amelynek célja a statikus vírusirtó elemzések (Static Analysis) kijátszása. A script egy egyszerű, de hatékony **XOR titkosítást** és **Base64 kódolást** alkalmaz, hogy a rosszindulatú kódot (payload) felismerhetetlen adathalmazzá alakítsa.

A generált "Stub" (Hordozó) fájl a lemezen ártalmatlannak tűnik, és csak futás közben, a memóriában fejti vissza és hajtja végre az eredeti utasításokat.

## ⚙️ Features
* **Polymorphic Builder:** Minden generáláskor véletlenszerű (Random) titkosítókulcsot használ, így a kimeneti fájl hash lenyomata mindig más (Signature Evasion).
* **XOR Encryption:** A payload bájtjainak maszkolása a kulccsal.
* **Fileless Execution:** A visszafejtett kód soha nem íródik ki a merevlemezre; a Python `exec()` függvénye közvetlenül a memóriában (RAM) futtatja le.
* **Static Evasion:** Mivel a forráskódban nem szerepelnek gyanús kulcsszavak (pl. `ctypes`, `subprocess`, `socket`), a Defender statikus motorja nem jelez.

## 🛠 Usage
1. **Payload Generálása:**
   Nyisd meg a `payload_builder.py`-t, és írd be a kívánt Python kódot a `payload_code` változóba. Ezután futtasd a buildert:
   ```bash
   python payload_builder.py