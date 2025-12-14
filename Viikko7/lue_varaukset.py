#Hiljan muokkaamaa koodia
#Käytän sanakirjaa.
from datetime import datetime

def muunna_varaustiedot(varaus: list) -> dict:
    return {
        "varausId": int(varaus[0]),
        "nimi": varaus[1],
        "sähköposti": varaus[2],
        "puhelin": varaus[3],
        "varauksenPvm": datetime.strptime(varaus[4], "%Y-%m-%d").date(),
        "varauksenKlo": datetime.strptime(varaus[5], "%H:%M").time(),
        "varauksenKesto": int(varaus[6]),
        "hinta": float(varaus[7]),
        "varausVahvistettu": varaus[8].lower() == "true",
        "varattuTila": varaus[9],
        "varausLuotu": datetime.strptime(varaus[10], "%Y-%m-%d %H:%M:%S")
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
        if varaus["varausVahvistettu"]:
            print(f"- {varaus['nimi']}, {varaus['varattuTila']}, {varaus['varauksenPvm'].strftime('%d.%m.%Y')} klo {varaus['varauksenKlo'].strftime('%H.%M')}")
    print()

def pitkat_varaukset(varaukset: list[dict]):
    for varaus in varaukset:
        if varaus["varauksenKesto"] >= 3:
            print(f"- {varaus['nimi']}, {varaus['varauksenPvm'].strftime('%d.%m.%Y')} klo {varaus['varauksenKlo'].strftime('%H.%M')}, kesto {varaus['varauksenKesto']} h, {varaus['varattuTila']}")
    print()

def varausten_vahvistusstatus(varaukset: list[dict]):
    for varaus in varaukset:
        status = "Vahvistettu" if varaus["varausVahvistettu"] else "EI vahvistettu"
        print(f"{varaus['nimi']} → {status}")
    print()

def varausten_lkm(varaukset: list[dict]):
    vahvistetut = sum(1 for v in varaukset if v["varausVahvistettu"])
    ei_vahvistetut = len(varaukset) - vahvistetut
    print(f"- Vahvistettuja varauksia: {vahvistetut} kpl")
    print(f"- Ei-vahvistettuja varauksia: {ei_vahvistetut} kpl")
    print()

def varausten_kokonaistulot(varaukset: list[dict]):
    tulot = sum(v["varauksenKesto"] * v["hinta"] for v in varaukset if v["varausVahvistettu"])
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
