"""
Ohjelma joka lukee tiedostossa olevat varaustiedot
ja tulostaa ne konsoliin käyttäen funkitoita.
Alla esimerkkitulostus:

Varausnumero: 123
Varaaja: Anna Virtanen
Päivämäärä: 31.10.2025
Aloitusaika: 10.00
Tuntimäärä: 2
Tuntihinta: 19,95 €
Kokonaishinta: 39,90 €
Maksettu: Kyllä
Kohde: Kokoustila A
Puhelin: 0401234567
Sähköposti: anna.virtanen@example.com

"""
from datetime import datetime

def hae_varaaja(varaus):
    nimi = varaus[1]
    print(f"Varaaja: {nimi}")

def hae_paiva(varaus):
    paiva = datetime.strptime(varaus[2].strip(), "%Y-%m-%d")
    print(f"Päivämäärä: {paiva.strftime('%d.%m.%Y')}")

def hae_varausnumero(varaus):
    varausnumero = varaus[0]
    print(f"Varausnumero: {varausnumero}")

def hae_aloitusaika(varaus):
    aloitusaika = varaus[3]
    print(f"Aloitusaika: {aloitusaika}")

def hae_tuntimaara(varaus):
    tuntimaara = varaus[4]
    print(f"Tuntimäärä: {tuntimaara}")

def hae_tuntihinta(varaus):
    tuntihinta = varaus[5]
    print(f"Tuntihinta: {tuntihinta}")

def laske_kokonaishinta(varaus):

    #Muunnetaan tuntimäärä ja tuntihinta numeroiksi
    tuntimaara = int(varaus[4])
    tuntihinta_str = varaus[5].replace("€", "").replace(",", ".").strip()
    tuntihinta = float(tuntihinta_str)

    #Lasketaan kokonaishinta
    kokonaishinta = tuntimaara * tuntihinta
    print(f"Kokonaishinta: {kokonaishinta:.2f} €")

def hae_maksettu(varaus):
    maksettu_str = varaus[6].strip().lower()  # esim. "true" tai "false"
    if maksettu_str == "true":
        print("Maksettu: Kyllä")
    else:
        print("Maksettu: Ei")

def hae_kohde(varaus):
    tila = varaus[7]
    print(f"Varattu tila: {tila}")

def hae_puhelin(varaus):
    puhelin = varaus[8]
    print(f"Puhelinnumero: {puhelin}")

def hae_sahkoposti(varaus):
    sahkoposti = varaus[9]
    print(f"Sähköposti: {sahkoposti}")

def main():
    # Maaritellaan tiedoston nimi suoraan koodissa
    varaukset = "varaukset.txt"

    # Avataan tiedosto, luetaan ja splitataan sisalto
    with open(varaukset, "r", encoding="utf-8") as f:
        varaus = f.read().strip()
        varaus = varaus.split('|')

    # Toteuta loput funktio hae_varaaja(varaus) mukaisesti
    # Luotavat funktiota tekevat tietotyyppien muunnoksen
    # ja tulostavat esimerkkitulosteen mukaisesti

    hae_varausnumero(varaus)
    hae_varaaja(varaus)
    hae_paiva(varaus)
    hae_aloitusaika(varaus)
    hae_tuntimaara(varaus)
    hae_tuntihinta(varaus)
    laske_kokonaishinta(varaus)
    hae_maksettu(varaus)
    hae_kohde(varaus)
    hae_puhelin(varaus)
    hae_sahkoposti(varaus)

if __name__ == "__main__":
    main()