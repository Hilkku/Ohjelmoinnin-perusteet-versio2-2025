# Pieni Python-ohjelma, joka lukee tiedoston ja tulostaa sen sisältämän sanan.
# Tässä versiossa on main-funktio ja if __name__ == "__main__" -lohko.

def main():
    # Määritellään tiedoston nimi suoraan koodissa
    tiedosto = "sana.txt"

    # Avataan tiedosto ja luetaan sisältö
    with open(tiedosto, "r", encoding="utf-8") as f:
        sana = f.read().strip()

    # Tulostetaan sana konsoliin
    print(sana)


# Tämä lohko varmistaa, että ohjelma suoritetaan vain,
# kun tiedostoa ajetaan suoraan, ei tuotaessa moduulina.
if __name__ == "__main__":
    main()