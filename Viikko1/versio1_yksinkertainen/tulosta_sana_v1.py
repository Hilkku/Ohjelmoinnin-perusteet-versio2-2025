# Yksinkertainen esimerkki Python-ohjelmasta,
# joka lukee tiedoston ja tulostaa sen sisältämän sanan.

# Määritellään tiedoston polku suoraan koodissa
tiedosto = "sana.txt"

# Avataan tiedosto ja luetaan sisältö
with open(tiedosto, "r", encoding="utf-8") as f:
    sana = f.read().strip()

# Tulostetaan sana konsoliin
print(sana)