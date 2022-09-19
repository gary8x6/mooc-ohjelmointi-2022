# Tee ratkaisusi tähän:

class Tehtava:

    iidee = 1

    def __init__(self, kuvaus: str, koodari: str, tyomaara: int):

        self.__kuvaus = kuvaus
        self.__koodari = koodari
        self.__tyomaara = tyomaara
        self.__valmis = False
        self.__id = Tehtava.iidee

        Tehtava.iidee += 1


    def __str__(self):

        if self.__valmis == True:
            status = "VALMIS"
        else:
            status = "EI VALMIS"

        return f"{self.__id}: {self.__kuvaus} ({self.__tyomaara} tuntia), koodari {self.__koodari} {status}"

    def on_valmis(self):

        return self.__valmis

    def merkkaa_valmiiksi(self):

        self.__valmis = True

    @property
    def kuvaus(self):
        return self.__kuvaus

    @property
    def id(self):
        return self.__id

    @property
    def koodari(self):
        return self.__koodari

    @property
    def tyomaara(self):
        return self.__tyomaara


class Tilauskirja():

    def __init__(self):
        self.__tehtavat = {}
        self.__koodarit = []

    def lisaa_tilaus(self, kuvaus: str, koodari: str, tyomaara: int):

        self.__tehtavat[Tehtava.iidee - 1] = Tehtava(kuvaus, koodari, tyomaara)
        if koodari not in self.__koodarit:
            self.__koodarit.append(koodari)

    def kaikki_tilaukset(self):

        kaikki_tehtavat = []

        for value in self.__tehtavat:
            kaikki_tehtavat.append(self.__tehtavat[value])

        return kaikki_tehtavat

    def koodarit(self):

        return self.__koodarit

    def merkkaa_valmiiksi(self, id: int):

        try:
            self.__tehtavat[id].merkkaa_valmiiksi()
        except:
            raise ValueError

    def valmiit_tilaukset(self):

        valmiit = []

        for tilaus in self.__tehtavat:
            if self.__tehtavat[tilaus].on_valmis() == True:
                valmiit.append(self.__tehtavat[tilaus])

        return valmiit


    def ei_valmiit_tilaukset(self):

        ei_valmiit = []

        for tilaus in self.__tehtavat:
            if self.__tehtavat[tilaus].on_valmis() == False:
                ei_valmiit.append(self.__tehtavat[tilaus])

        return ei_valmiit

    def koodarin_status(self, nimi: str):

        if nimi not in self.__koodarit:
            raise ValueError


        valmiina = 0
        ei_valmiina = 0
        valmis_aika = 0
        ei_valmis_aika = 0

        for tilaus in self.__tehtavat:
        
                if self.__tehtavat[tilaus].koodari == nimi:

                    if self.__tehtavat[tilaus].on_valmis():
                        valmiina += 1
                        valmis_aika += self.__tehtavat[tilaus].tyomaara

                    if self.__tehtavat[tilaus].on_valmis() == False:
                        ei_valmiina += 1
                        ei_valmis_aika += self.__tehtavat[tilaus].tyomaara


                

        return (valmiina, ei_valmiina, valmis_aika, ei_valmis_aika)
                


if __name__ == "__main__":
    tilaukset = Tilauskirja()
    tilaukset.lisaa_tilaus("koodaa webbikauppa", "Antti", 10)
    tilaukset.lisaa_tilaus("tee mobiilisovellus työaikakirjanpitoon", "Antti", 25)
    tilaukset.lisaa_tilaus("tee ohjelma matematiikan harjoitteluun", "Antti", 100)
    tilaukset.lisaa_tilaus("tee uusi facebook", "Erkki", 1000)

    tilaukset.merkkaa_valmiiksi(1)
    tilaukset.merkkaa_valmiiksi(2)

    status = tilaukset.koodarin_status("Jere")
    print(status)