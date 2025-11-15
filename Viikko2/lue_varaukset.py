"""
Ohjelma joka lukee tiedostossa olevat varaustiedot
ja tulostaa ne konsoliin. Alla esimerkkitulostus:

Varausnumero: 123
Varaaja: Anna Virtanen
Päivämäärä: 31.10.2025
Aloitusaika: 10.00
Tuntimäärä: 2
Tuntihinta: 19.95 €
Kokonaishinta: 39.9 €
Maksettu: Kyllä
Kohde: Kokoustila A
Puhelin: 0401234567
Sähköposti: anna.virtanen@example.com

"""

from datetime import datetime

def main():
    varaukset = "varaukset.txt"

    # Avataan tiedosto ja luetaan sisältö
    with open(varaukset, "r", encoding="utf-8") as f:
        varaus = f.read().strip()

    # Pilkotaan tiedot listaksi
    tiedot = varaus.split('|')

    # Muotoillaan päivämäärä ja aika
    paiva = datetime.strptime(tiedot[2], "%Y-%m-%d")
    suomalainenPaiva = paiva.strftime("%d.%m.%Y")

    aika = datetime.strptime(tiedot[3], "%H:%M")
    suomalainenAika = aika.strftime("%H.%M")

    # Maksettu-kenttä
    maksettu = "Kyllä" if tiedot[6].strip().lower() in ["kyllä", "true", "1"] else "Ei"

    # Tulostetaan tiedot halutussa muodossa
    print(f"Varausnumero: {tiedot[0]}")
    print(f"Varaaja: {tiedot[1]}")
    print(f"Päivämäärä: {suomalainenPaiva}")
    print(f"Aloitusaika: {suomalainenAika}")
    print(f"Tuntimäärä: {tiedot[4]}")
    print(f"Tuntihinta: {tiedot[5]} €")
    print(f"Maksettu: {maksettu}")
    print(f"Kohde: {tiedot[7]}")
    print(f"Puhelin: {tiedot[8]}")
    print(f"Sähköposti: {tiedot[9]}")

if __name__ == "__main__":
    main()