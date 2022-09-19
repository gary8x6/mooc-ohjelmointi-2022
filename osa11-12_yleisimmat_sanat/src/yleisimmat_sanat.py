# TEE RATKAISUSI TÄHÄN:
def yleisimmat_sanat(tiedoston_nimi: str, raja: int):

    with open(tiedoston_nimi, "r") as f:
        vanha_teksti = f.read()   

    spessu = ",.-'â€™"
    teksti = ""

    for kirjain in vanha_teksti:
        if kirjain not in spessu:
            teksti = teksti + kirjain

    teksti = teksti.replace("\n", " ")
    teksti = teksti.split(" ")
    #print(teksti)


    palautus = {sana: teksti.count(sana) for sana in teksti if teksti.count(sana) >= raja}

    return palautus
    
    


if __name__ == "__main__":
    #with open("comprehensions.txt", "r") as f:
     #   teksti = f.read()

    yleisimmat_sanat("comprehensions.txt", 3)