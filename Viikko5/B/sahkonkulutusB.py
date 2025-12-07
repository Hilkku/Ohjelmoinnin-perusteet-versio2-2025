
# Copyright (c) 2025 Hilja Liukkonen
# License: MIT

from datetime import datetime
from typing import Dict, List, Tuple
#tyyppivihjeiden työkalut käyttöön Pythonille.

# Sanakirja englanti → suomi. Käytän sanakirjaa, koska se kuulosti helpoimmalta vaihtoehdolta. 
# Jos käännettävää olisi paljon, täytyisi keksiä toinen tapa.
paivien_nimet: Dict[str, str] = {
    "Monday": "maanantai",
    "Tuesday": "tiistai",
    "Wednesday": "keskiviikko",
    "Thursday": "torstai",
    "Friday": "perjantai",
    "Saturday": "lauantai",
    "Sunday": "sunnuntai"
}

def lue_data(tiedosto: str) -> Dict[str, Tuple[str, List[float]]]:
    """Lukee CSV-tiedoston ja palauttaa sanakirjan."""
    data: Dict[str, Tuple[str, List[float]]] = {}
    with open(tiedosto, "r", encoding="utf-8") as f:
        next(f)  #Ohita otsikkorivi, joka erilainen.
        for line in f:
            aika, k1, k2, k3, t1, t2, t3 = line.strip().split(";")
            dt: datetime = datetime.fromisoformat(aika)
            eng_pv: str = dt.strftime("%A")
            suomi_pv: str = paivien_nimet[eng_pv]
            pvm: str = dt.strftime("%d.%m.%Y")
            arvot: List[float] = [int(k1)/1000, int(k2)/1000, int(k3)/1000,
                                  int(t1)/1000, int(t2)/1000, int(t3)/1000]
            if suomi_pv not in data:
                data[suomi_pv] = (pvm, [0, 0, 0, 0, 0, 0])
            nykyiset = data[suomi_pv][1]
            data[suomi_pv] = (pvm, [nykyiset[i] + arvot[i] for i in range(6)])
    return data

def muotoile_luku(arvo: float) -> str:
    """Muuntaa luvun kahden desimaalin tarkkuudelle ja käyttää pilkkua erottimena."""
    return f"{arvo:.2f}".replace(".", ",")

def kirjoita_yhteenveto(viikkodata: Dict[str, Dict[str, Tuple[str, List[float]]]], tiedosto: str) -> None:
    """Kirjoittaa yhteenvedon tiedostoon. Sisältää viikkoyhteenvedot sekä summat ja keskiarvot."""
    järjestys: List[str] = ["maanantai", "tiistai", "keskiviikko", "torstai",
                             "perjantai", "lauantai", "sunnuntai"]

    with open(tiedosto, "w", encoding="utf-8") as f:
        f.write("Yhteenveto viikoista 41–43 (kWh, vaiheittain)\n\n")

        kokonaissumma = [0, 0, 0, 0, 0, 0]
        paivien_lkm = 0

        for viikko, data in viikkodata.items():
            f.write(f"*** {viikko} ***\n")
            f.write(f"{'Päivä':<12}{'Pvm':<12}{'Kulutus [kWh]':<32}{'Tuotanto [kWh]'}\n")
            f.write(f"{'':<12}{'(pv.kk.vvvv)':<12}{'v1':>8}{'v2':>8}{'v3':>8}{'v1':>10}{'v2':>8}{'v3':>8}\n")
            f.write("-" * 75 + "\n")

            viikko_summa = [0, 0, 0, 0, 0, 0]

            for pv in järjestys:
                if pv in data:
                    pvm, arvot = data[pv]
                    kulutus = arvot[:3]
                    tuotanto = arvot[3:]
                    f.write(f"{pv:<12}{pvm:<12}" +
                            "".join(f"{muotoile_luku(x):>8}" for x in kulutus) +
                            "    " +
                            "".join(f"{muotoile_luku(x):>8}" for x in tuotanto) +
                            "\n")
                    viikko_summa = [viikko_summa[i] + arvot[i] for i in range(6)]
                    kokonaissumma = [kokonaissumma[i] + arvot[i] for i in range(6)]
                    paivien_lkm += 1

            #Viikon kokonaissumma
            f.write("-" * 75 + "\n")
            f.write("Viikon summa:\n")
            f.write(f"{'':<12}{'':<12}" +
                    "".join(f"{muotoile_luku(x):>8}" for x in viikko_summa[:3]) +
                    "    " +
                    "".join(f"{muotoile_luku(x):>8}" for x in viikko_summa[3:]) +
                    "\n\n")

        #Lopuksi kokonaissummat ja keskiarvot
        f.write("=" * 75 + "\n")
        f.write("KOKONAISSUMMAT (viikot 41–43):\n")
        f.write(f"{'':<12}{'':<12}" +
                "".join(f"{muotoile_luku(x):>8}" for x in kokonaissumma[:3]) +
                "    " +
                "".join(f"{muotoile_luku(x):>8}" for x in kokonaissumma[3:]) +
                "\n")

        f.write("\nKeskiarvot per päivä:\n")
        if paivien_lkm > 0:
            keskiarvot = [x / paivien_lkm for x in kokonaissumma]
            f.write(f"{'':<12}{'':<12}" +
                    "".join(f"{muotoile_luku(x):>8}" for x in keskiarvot[:3]) +
                    "    " +
                    "".join(f"{muotoile_luku(x):>8}" for x in keskiarvot[3:]) +
                    "\n")

def main() -> None:
    tiedostot = {
        "Viikko 41": lue_data("viikko41.csv"),
        "Viikko 42": lue_data("viikko42.csv"),
        "Viikko 43": lue_data("viikko43.csv")
    }
    kirjoita_yhteenveto(tiedostot, "yhteenveto.txt")

if __name__ == "__main__":
    main()
