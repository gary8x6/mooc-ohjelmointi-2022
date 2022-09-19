# tee ratkaisusi tänne
# jos käytät edellisessä tehtävässä tekemiäsi luokkia, kopioi ne tänne
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
            self.__tehtavat[int(id)].merkkaa_valmiiksi()
        except:
            return False

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
                        valmis_aika += int(self.__tehtavat[tilaus].tyomaara)

                    if self.__tehtavat[tilaus].on_valmis() == False:
                        ei_valmiina += 1
                        ei_valmis_aika += int(self.__tehtavat[tilaus].tyomaara)


                

        return (valmiina, ei_valmiina, valmis_aika, ei_valmis_aika)

class Tilauskirjasovellus:

    def __init__(self):
        self.__tilauskirja = Tilauskirja()

    def valikko(self):
        print("komennot:")
        print("0 lopetus")
        print("1 lisää tilaus")
        print("2 listaa valmiit")
        print("3 listaa ei valmiit")
        print("4 merkitse tehtävä valmiiksi")
        print("5 koodarit")
        print("6 koodarin status")

    def lisaa_tilaus(self):
        kuvaus = input("kuvaus: ")
        koodari_tyo = input("koodari ja työmääräarvio: ")
        koodari_tyo = koodari_tyo.split(" ")

        if len(koodari_tyo) != 2:
            print("virheellinen syöte")
            return
        
        if not koodari_tyo[1].isnumeric():
            print("virheellinen syöte")
            return


        self.__tilauskirja.lisaa_tilaus(kuvaus, koodari_tyo[0], koodari_tyo[1])
        print("lisätty!")

    def listaa_valmiit(self):
        lista = self.__tilauskirja.valmiit_tilaukset()

        if lista != []:
        
            for item in lista:
                print(item)

        else:

            print("ei valmiita")

    def listaa_ei_valmiit(self):
        lista = self.__tilauskirja.ei_valmiit_tilaukset()

        for item in lista:
            print(item)

    def merkitse_valmiiksi(self):
        iidee = input("tunniste: ")
        if not iidee.isnumeric():
            print("virheellinen syöte")
            return

        if self.__tilauskirja.merkkaa_valmiiksi(iidee) == False:
            print("virheellinen syöte")
            return
        
        self.__tilauskirja.merkkaa_valmiiksi(iidee)
        print("merkitty valmiiksi")

    def koodarit(self):
        lista = self.__tilauskirja.koodarit()

        for koodari in lista:
            print(koodari)

    def koodarin_status(self):
        nimi = input("koodari: ")
        if nimi in self.__tilauskirja.koodarit():
            status = self.__tilauskirja.koodarin_status(nimi)

            print(f"työt: valmiina {status[0]} ei valmiina {status[1]}, tunteja: tehty {status[2]} tekemättä {status[3]}")
        else:
            print("virheellinen syöte")
            return

    def suorita(self):
        self.valikko()
        while True:
            #print("")
            komento = input("komento: ")
            if komento == "0":
                break
            elif komento == "1":
                self.lisaa_tilaus()
            elif komento == "2":
                self.listaa_valmiit()
            elif komento == "3":
                self.listaa_ei_valmiit()
            elif komento == "4":
                self.merkitse_valmiiksi()
            elif komento == "5":
                self.koodarit()
            elif komento == "6":
                self.koodarin_status()
            else:
                self.valikko()

sovellus = Tilauskirjasovellus()
sovellus.suorita()