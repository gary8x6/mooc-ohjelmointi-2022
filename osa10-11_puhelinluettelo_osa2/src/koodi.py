
# Tee ratkaisusi tähän:
class Henkilo:

    def __init__(self, nimi: str):

        self.__nimi = nimi
        self.__numerot = []
        self.__osoite = None

    def nimi(self):

        return self.__nimi

    def numerot(self):

        return self.__numerot

    def osoite(self):

        return self.__osoite

    def lisaa_numero(self, numero: str):

        self.__numerot.append(numero)

    def lisaa_osoite(self, osoite: str):

        self.__osoite = osoite

class Puhelinluettelo:
    def __init__(self):
        self.__henkilot = {}

    def lisaa_numero(self, nimi: str, numero: str):
        if not nimi in self.__henkilot:
            self.__henkilot[nimi] = Henkilo(nimi)

        self.__henkilot[nimi].lisaa_numero(numero)

    def lisaa_osoite(self, nimi: str, osoite: str):
        if not nimi in self.__henkilot:
            self.__henkilot[nimi] = Henkilo(nimi)

        self.__henkilot[nimi].lisaa_osoite(osoite)


    def hae_tiedot(self, nimi: str):
        if not nimi in self.__henkilot:
            return None, None

        return (self.__henkilot[nimi].numerot(), self.__henkilot[nimi].osoite())

    def kaikki_tiedot(self):
        return self.__henkilot

class PuhelinluetteloSovellus:
    def __init__(self):
        self.__luettelo = Puhelinluettelo()

    def ohje(self):
        print("komennot: ")
        print("0 lopetus")
        print("1 numeron lisäys")
        print("2 haku")
        print("3 osoitteen lisäys")

    def numeron_lisays(self):
        nimi = input("nimi: ")
        numero = input("numero: ")
        self.__luettelo.lisaa_numero(nimi, numero)

    def osoitteen_lisays(self):
        nimi = input("nimi: ")
        osoite = input("osoite: ")
        self.__luettelo.lisaa_osoite(nimi, osoite)

    def haku(self):
        
        nimi = input("nimi: ")
        numerot, osoite = self.__luettelo.hae_tiedot(nimi)

        
        if numerot == None or numerot == []:
            print("numero ei tiedossa")
        else:
            for numero in numerot:
                print(numero)
        
        if osoite == None:
            print("osoite ei tiedossa")
        else:
            print(osoite)

        return   

    def suorita(self):
        self.ohje()
        while True:
            print("")
            komento = input("komento: ")
            if komento == "0":
                break
            elif komento == "1":
                self.numeron_lisays()
            elif komento == "2":
                self.haku()
            elif komento == "3":
                self.osoitteen_lisays()
            else:
                self.ohje()





# kun testaat, mitään muuta koodia ei saa olla luokkien ulkopuolella kuin seuraavat rivit
sovellus = PuhelinluetteloSovellus()
sovellus.suorita()
