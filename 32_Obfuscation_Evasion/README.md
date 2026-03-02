# ⚠️ LEGAL DISCLAIMER

**HU:** Ez az eszköz kizárólag **saját rendszerek tesztelésére** vagy a tulajdonos írásos engedélyével rendelkező hálózatokon használható. A szoftver oktatási céllal készült. A szerző (Paczok Norisz) elhárít minden felelősséget a jogellenes használatért vagy károkért.

**EN:** This tool is for **educational purposes and authorized testing only**. The creator (Paczok Norisz) assumes no liability for misuse or any damage caused by this program.

---

# 🎭 Project 32: Payload Obfuscator (AV Evasion)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square)
![Technique](https://img.shields.io/badge/Technique-XOR%2FBase64-orange?style=flat-square)
![Category](https://img.shields.io/badge/Category-Defense_Evasion-red?style=flat-square)

## 📌 Áttekintés (Overview)
Ez a projekt az **Obfuscation (Kódzavarás)** technikáit demonstrálja. A cél a biztonsági szoftverek (AV/EDR) kijátszása a kártékony payload (pl. shellcode) olvashatatlanná tételével. A program Base64 kódolást és XOR titkosítást alkalmaz, hogy elrejtse a kód valódi szándékát a statikus elemzők elől.

## 🛠️ Funkciók
* **📦 Multi-Layer Encoding:** Base64 és XOR kombinált használata.
* **🔑 Custom XOR Key:** Egyedi kulcs generálása a titkosításhoz.
* **📝 Payload Generation:** Futtatható Python stub generálása, amely a memóriában dekódolja önmagát.

## ⚙️ Technikai Részletek
* **Nyelv:** Python 3.x
* **Algoritmus:** Rolling XOR + Base64
* **Cél:** Signature-based detection (Aláírás alapú védelem) megkerülése.

## 🚀 Használat
```bash
python payload_builder.py
