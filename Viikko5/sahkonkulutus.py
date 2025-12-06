
from datetime import datetime
from collections import defaultdict

def lue_data(tiedosto: str) -> dict:
    """Lukee CSV-tiedoston ja palauttaa sanakirjan, jossa avaimena viikonpäivä ja arvona summat."""
    data = defaultdict(lambda: [0, 0, 0, 0, 0, 0])  # kulutus 3 vaihetta + tuotanto 3 vaihetta
    with open(tiedosto, "r", encoding="utf-8") as f:
        next(f)  # ohita otsikkorivi
        for line in f:
            aika, k1, k2, k3, t1, t2, t3 = line.strip().split(";")
            päivä = datetime.fromisoformat(aika).strftime("%A")  # esim. Monday
            arvot = [int(k1)/1000, int(k2)/1000, int(k3)/1000, int(t1)/1000, int(t2)/1000, int(t3)/1000]
            data[päivä] = [data[päivä][i] + arvot[i] for i in range(6)]
    return data

def tulosta_raportti(data: dict) -> None:
    """Tulostaa sähkönkulutus- ja tuotantotiedot taulukkona."""
    järjestys = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    print("\nSähkönkulutus ja -tuotanto (kWh) per viikonpäivä:\n")
    print(f"{'Päivä':<10} {'Kulutus1':>10} {'Kulutus2':>10} {'Kulutus3':>10} {'Tuotanto1':>10} {'Tuotanto2':>10} {'Tuotanto3':>10}")
    for pv in järjestys:
        if pv in data:
            arvot = data[pv]
            print(f"{pv:<10} " + " ".join(f"{x:>10.2f}" for x in arvot))

def main() -> None:
    """Ohjelman pääfunktio: lukee datan, laskee yhteenvedot ja tulostaa raportin."""
    tiedosto = "viikko42.csv"
    data = lue_data(tiedosto)
    tulosta_raportti(data)

if __name__ == "__main__":
    main()
