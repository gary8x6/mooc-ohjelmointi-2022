# tee ratkaisusi tänne
class Kurssi:

    def __init__(self, nimi: str):
        self.__nimi = nimi
        self.__arvosana = 0
        self.__opintopisteet = 0

    def nimi(self):

        return self.__nimi
    
    def arvosana(self):

        return self.__arvosana

    def opintopisteet(self):

        return self.__opintopisteet

    def lisaa_arvosana(self, arvosana: int):

        self.__arvosana = arvosana
        

    def lisaa_opintopiste(self, opintopisteet):

        self.__opintopisteet = opintopisteet


class Opintorekisteri:

    def __init__(self):
        self.__kurssit = {}

    def lisaa_suoritus(self, kurssi: str, arvosana: int, opintopisteet: int):
        if not kurssi in self.__kurssit:
            self.__kurssit[kurssi] = Kurssi(kurssi)

        if self.__kurssit[kurssi].arvosana() < int(arvosana):
                self.__kurssit[kurssi].lisaa_arvosana(arvosana)

        self.__kurssit[kurssi].lisaa_opintopiste(opintopisteet)

    def hae_suoritus(self, kurssi: str):
        if not kurssi in self.__kurssit:
            return None, None, None

        return (self.__kurssit[kurssi].nimi(), self.__kurssit[kurssi].arvosana(), self.__kurssit[kurssi].opintopisteet())

    def tilastot(self):

        suoritukset = 0
        opintopisteet = 0
        arvosana = 0
        jakauma = {5: 0, 4: 0, 3: 0, 2: 0 ,1: 0}
        arvosanat_yht = 0

        
        for kurssi in self.__kurssit:
            arvosana = self.__kurssit[kurssi].arvosana()
            opintopisteet += self.__kurssit[kurssi].opintopisteet()
            suoritukset += 1
            jakauma[arvosana] += 1
            arvosanat_yht += arvosana

        keskiarvo = arvosanat_yht / suoritukset


        print(f"suorituksia {suoritukset} kurssilta, yhteensä {opintopisteet} opintopistettä")
        print(f"keskiarvo {keskiarvo:.1f}")
        print("arvosanajakauma")
        for key in jakauma:
            xxses = ""
            for times in range(jakauma[key]):
                xxses = xxses + "x"
            print(f"{key}: {xxses}")





class OpintorekisteriSovellus:

    def __init__(self):
        self.__opintorekisteri = Opintorekisteri()


    def ohje(self):
        print("Komennot:")
        print("1 lisää suoritus")
        print("2 hae suoritus")
        print("3 tilastot")
        print("0 lopetus")

    def lisaa_suoritus(self):
        kurssi = input("kurssi: ")
        arvosana = input("arvosana: ")
        opintopisteet = input("opintopisteet: ")

        self.__opintorekisteri.lisaa_suoritus(kurssi, int(arvosana), int(opintopisteet))

    def haku(self):
        kurssi = input("kurssi: ")

        nimi, arvosana, opintopiste = self.__opintorekisteri.hae_suoritus(kurssi)

        if nimi == None:
            print("ei suoritusta")
            return

        print(f"{nimi} ({opintopiste} op) arvosana {arvosana}")

        return

    def tilasto(self):

        self.__opintorekisteri.tilastot()

        pass

    def suorita(self):
        self.ohje()
        while True:
            print("")
            komento = input("Komento: ")

            if komento == "0":
                break
            elif komento == "1":
                self.lisaa_suoritus()
            elif komento == "2":
                self.haku()
            elif komento == "3":
                self.tilasto()
            else:
                self.ohje()

sovellus = OpintorekisteriSovellus()
sovellus.suorita()