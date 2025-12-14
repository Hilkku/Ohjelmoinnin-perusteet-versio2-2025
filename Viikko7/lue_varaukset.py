#Hiljan muokkaamaa koodia
#Käytän sanakirjaa.
from datetime import datetime

def muunna_varaustiedot(varaus: list) -> dict:
    return {
        "VarausId": int(varaus[0]),
        "Nimi": varaus[1],
        "Sähköposti": varaus[2],
        "Puhelin": varaus[3],
        "VarauksenPvm": datetime.strptime(varaus[4], "%Y-%m-%d").date(),
        "VarauksenKlo": datetime.strptime(varaus[5], "%H:%M").time(),
        "VarauksenKesto": int(varaus[6]),
        "Hinta": float(varaus[7]),
        "VarausVahvistettu": varaus[8].lower() == "true",
        "VarattuTila": varaus[9],
        "VarausLuotu": datetime.strptime(varaus[10], "%Y-%m-%d %H:%M:%S")
    }

def hae_varaukset(varaustiedosto: str) -> list[dict]:
    varaukset = []
    with open(varaustiedosto, "r", encoding="utf-8") as f:
        for rivi in f:
            varaustiedot = rivi.strip().split('|')
            varaukset.append(muunna_varaustiedot(varaustiedot))
    return varaukset

def vahvistetut_varaukset(varaukset: list[dict]):
    for varaus in varaukset:
        if varaus["VarausVahvistettu"]:
            print(f"- {varaus['Nimi']}, {varaus['VarattuTila']}, {varaus['VarauksenPvm'].strftime('%d.%m.%Y')} klo {varaus['VarauksenKlo'].strftime('%H.%M')}")
    print()

def pitkat_varaukset(varaukset: list[dict]):
    for varaus in varaukset:
        if varaus["VarauksenKesto"] >= 3:
            print(f"- {varaus['Nimi']}, {varaus['VarauksenPvm'].strftime('%d.%m.%Y')} klo {varaus['VarauksenKlo'].strftime('%H.%M')}, kesto {varaus['VarauksenKesto']} h, {varaus['VarattuTila']}")
    print()

def varausten_vahvistusstatus(varaukset: list[dict]):
    for varaus in varaukset:
        status = "Vahvistettu" if varaus["VarausVahvistettu"] else "EI vahvistettu"
        print(f"{varaus['Nimi']} → {status}")
    print()

def varausten_lkm(varaukset: list[dict]):
    vahvistetut = sum(1 for v in varaukset if v["VarausVahvistettu"])
    ei_vahvistetut = len(varaukset) - vahvistetut
    print(f"- Vahvistettuja varauksia: {vahvistetut} kpl")
    print(f"- Ei-vahvistettuja varauksia: {ei_vahvistetut} kpl")
    print()

def varausten_kokonaistulot(varaukset: list[dict]):
    tulot = sum(v["VarauksenKesto"] * v["Hinta"] for v in varaukset if v["VarausVahvistettu"])
    print("Vahvistettujen varausten kokonaistulot:", f"{tulot:.2f}".replace('.', ','), "€")
    print()

def main():
    varaukset = hae_varaukset("varaukset.txt")
    print("1) Vahvistetut varaukset")
    vahvistetut_varaukset(varaukset)
    print("2) Pitkät varaukset (≥ 3 h)")
    pitkat_varaukset(varaukset)
    print("3) Varausten vahvistusstatus")
    varausten_vahvistusstatus(varaukset)
    print("4) Yhteenveto vahvistuksista")
    varausten_lkm(varaukset)
    print("5) Vahvistettujen varausten kokonaistulot")
    varausten_kokonaistulot(varaukset)

if __name__ == "__main__":
    main()
