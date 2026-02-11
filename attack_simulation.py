import os
import time
import sys

def banner():
    os.system("cls")
    print("""
    ██╗      ███████╗██╗   ██╗███████╗██╗          ██╗  ██╗
    ██║      ██╔════╝██║   ██║██╔════╝██║          ██║  ██║
    ██║      █████╗  ██║   ██║█████╗  ██║          ███████║
    ██║      ██╔══╝  ╚██╗ ██╔╝██╔══╝  ██║          ╚════██║
    ███████╗███████╗ ╚████╔╝ ███████╗███████╗██╗        ██║
    ╚══════╝╚══════╝  ╚═══╝  ╚══════╝╚══════╝╚═╝        ╚═╝
    --- INTEGRATED ATTACK CHAIN SIMULATION ---
    """)

def step_msg(step, name, description):
    print(f"\n[{step}/5] >>> {name}")
    print(f"       Cél: {description}")
    input("       [Nyomj Entert az indításhoz...]")

def run_module(path, script_name, args=""):
    full_path = os.path.join(path, script_name)
    if os.path.exists(full_path):
        print(f"       [*] Futtatás: {script_name}...")
        time.sleep(1)
        # Windows parancs: python "utvonal\script.py" argumentumok
        os.system(f'python "{full_path}" {args}')
    else:
        print(f"       [!] HIBA: Nem találom a fájlt: {full_path}")

def main():
    base_dir = os.getcwd() # A Level 4 gyökér
    
    banner()
    print("[*] Üdvözöllek a Level 4 vizsgán, Norisz.")
    print("[*] A célpont a SAJÁT géped (Localhost Simulation).")
    print("[*] Indul a Kill Chain...\n")

    # --- STEP 1: OBFUSCATION (Payload Generálás) ---
    step_msg(1, "WEAPONIZATION", "FUD Payload generálása (Rejtőzködés)")
    # Belépünk a 32-es mappába és futtatjuk a buildert
    obf_dir = os.path.join(base_dir, "32_Obfuscation_Evasion")
    run_module(obf_dir, "payload_builder.py")
    
    # --- STEP 2: PERSISTENCE (Beágyazódás) ---
    step_msg(2, "PERSISTENCE", "A Payload rögzítése (Registry & Startup)")
    pers_dir = os.path.join(base_dir, "30_Persistence_Mechanisms")
    run_module(pers_dir, "persistence_toolkit.py")
    
    # --- STEP 3: PRIVILEGE ESCALATION (Jogosultság szerzés) ---
    step_msg(3, "PRIVILEGE ESCALATION", "UAC Bypass (Admin jogok)")
    priv_dir = os.path.join(base_dir, "31_Privilege_Escalation")
    run_module(priv_dir, "uac_bypass.py")
    
    # --- STEP 4: CREDENTIAL ACCESS (Adatlopás) ---
    step_msg(4, "CREDENTIAL ACCESS", "Böngésző jelszavak kinyerése")
    cred_dir = os.path.join(base_dir, "33_Credential_Harvesting")
    run_module(cred_dir, "chrome_thief.py")
    
    # --- STEP 5: ANTI-FORENSICS (Nyomeltüntetés) ---
    step_msg(5, "DEFENSE EVASION", "Loot fájl időbélyegének meghamisítása")
    anti_dir = os.path.join(base_dir, "34_Anti_Forensics")
    
    # A zsákmány fájl helye (a Credential mappában jött létre)
    loot_file = os.path.join(cred_dir, "megszerzett_jelszavak.txt")
    
    if os.path.exists(loot_file):
        print(f"       [*] A zsákmány megtalálva: {loot_file}")
        print("       [*] Átadjuk a Timestompernek...")
        
        # Itt egy kis trükk: A timestomper interaktív, de mi most átadjuk neki paraméterben?
        # Mivel a timestomper-t interaktívra írtuk, itt most csak elindítjuk, 
        # neked kell majd beírni/bemásolni az útvonalat kézzel, vagy átírjuk a timestomper-t argumentum-kezelősre.
        # Most az egyszerűség kedvéért: elindítom, te pedig másold be neki a fenti útvonalat!
        
        run_module(anti_dir, "timestomper.py")
    else:
        print("       [!] Nem találtam meg a jelszófájlt, lehet, hogy a 4. lépés nem sikerült?")

    print("\n=======================================================")
    print("   [🏆] MISSION ACCOMPLISHED - LEVEL 4 COMPLETED")
    print("=======================================================")

if __name__ == "__main__":
    main()