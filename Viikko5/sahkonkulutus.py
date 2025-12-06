
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
        next(f)  #Ohita otsikkorivi, joka erilainen kuin muut rivit.
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
            #Päivitä summat
            nykyiset = data[suomi_pv][1]
            data[suomi_pv] = (pvm, [nykyiset[i] + arvot[i] for i in range(6)])
    return data

def muotoile_luku(arvo: float) -> str:
    """Muuntaa luvun kahden desimaalin tarkkuudelle ja käyttää pilkkua erottimena."""
    return f"{arvo:.2f}".replace(".", ",")

def tulosta_raportti(data: Dict[str, Tuple[str, List[float]]]) -> None:
    """Tulostaa taulukon halutussa muodossa."""
    järjestys: List[str] = ["maanantai", "tiistai", "keskiviikko", "torstai",
                             "perjantai", "lauantai", "sunnuntai"]
    print("\nViikon 42 sähkönkulutus ja -tuotanto (kWh, vaiheittain)\n")
    print(f"{'Päivä':<12}{'Pvm':<12}{'Kulutus [kWh]':<32}{'Tuotanto [kWh]'}")
    print(f"{'':<12}{'(pv.kk.vvvv)':<12}{'v1':>8}{'v2':>8}{'v3':>8}{'v1':>10}{'v2':>8}{'v3':>8}")
    print("-" * 75)
    for pv in järjestys:
        if pv in data:
            pvm, arvot = data[pv]
            kulutus = arvot[:3]
            tuotanto = arvot[3:]
            print(f"{pv:<12}{pvm:<12}" +
                  "".join(f"{muotoile_luku(x):>8}" for x in kulutus) +
                  "    " +
                  "".join(f"{muotoile_luku(x):>8}" for x in tuotanto))

def main() -> None:
    """Ohjelman pääfunktio, joka tekee tulostuksen funktioiden muotoilujen avulla."""
    tiedosto: str = "viikko42.csv"
    data = lue_data(tiedosto)
    tulosta_raportti(data)

if __name__ == "__main__":
    main()
