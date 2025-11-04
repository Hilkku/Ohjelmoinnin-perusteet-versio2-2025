# Pieni Python-ohjelma, joka lukee tiedoston ja tulostaa sen sisältämän sanan.
# Tässä versiossa on main-funktio, virheenkäsittely ja if __name__ == "__main__" -lohko.

def main():
    tiedosto = "sana.txt"

    try:
        # Avataan tiedosto ja luetaan sisältö
        with open(tiedosto, "r", encoding="utf-8") as f:
            sana = f.read().strip()

        # Jos tiedosto on tyhjä
        if not sana:
            print("Virhe: tiedosto on tyhjä.")
            return

        # Tulostetaan sana konsoliin
        print(sana)

    except FileNotFoundError:
        print(f"Virhe: tiedostoa '{tiedosto}' ei löytynyt.")
    except PermissionError:
        print(f"Virhe: tiedostoon '{tiedosto}' ei ole lukuoikeutta.")
    except Exception as e:
        print(f"Tuntematon virhe: {e}")


if __name__ == "__main__":
    main()