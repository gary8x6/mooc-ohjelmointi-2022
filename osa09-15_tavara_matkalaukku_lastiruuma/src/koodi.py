# Tee ratkaisusi tähän:
class Tavara:

    def __init__(self, nimi: str, paino: int):

        self.__nimi = nimi
        self.__paino = paino

    def __str__(self):

        return f"{self.__nimi} ({self.__paino} kg)"

    def paino(self):

        return self.__paino

    def nimi(self):

        return self.__nimi



class Matkalaukku:

    def __init__(self, maksimipaino: int):

        self.tavarat = []
        self.maksimipaino = maksimipaino

    def __str__(self):

        yhteispaino = 0

        for tavara in self.tavarat:

            yhteispaino += int(tavara.paino())

        if len(self.tavarat) == 1:

            return f"{len(self.tavarat)} tavara ({yhteispaino} kg)"

        else:

            return f"{len(self.tavarat)} tavaraa ({yhteispaino} kg)"

    def lisaa_tavara(self, tavara: Tavara):

        yhteispaino = 0

        for item in self.tavarat:

            yhteispaino += int(item.paino())


        if yhteispaino + tavara.paino() <= self.maksimipaino:

            self.tavarat.append(tavara)

    def tulosta_tavarat(self):

        for item in self.tavarat:
            print(f"{item.nimi()} ({item.paino()} kg)")

    def paino(self):

        yhteispaino = 0

        for item in self.tavarat:

            yhteispaino += int(item.paino())

            
        return yhteispaino

    def raskain_tavara(self):

        raskain = 0
        romu = ""

        for item in self.tavarat:

            if item.paino() > raskain:
                raskain = item.paino()
                romu = item

        return romu


class Lastiruuma:

    def __init__(self, maksimipaino: int):

        self.maksimipaino = maksimipaino
        self.lasti = []

    def __str__(self):

        yhteispaino = 0

        for item in self.lasti:

            yhteispaino += int(item.paino())

        tilaa = self.maksimipaino - yhteispaino

        if tilaa < 0:

            tilaa == 0

        if len(self.lasti) == 1:

            return f"{len(self.lasti)} matkalaukku, tilaa {tilaa} kg"

        else:

            return f"{len(self.lasti)} matkalaukkua, tilaa {tilaa} kg"
        
    def lisaa_matkalaukku(self, laukku: Matkalaukku):

        yhteispaino = 0

        for item in self.lasti:

            yhteispaino += int(item.paino())

        tilaa = self.maksimipaino - yhteispaino

        if tilaa - laukku.paino() >= 0:

            self.lasti.append(laukku)

    def tulosta_tavarat(self):

        if len(self.lasti) > 0:

            for laukku in self.lasti:

                laukku.tulosta_tavarat()

            






if __name__ == "__main__":

    

    tavara = Tavara("Aapiskukko", 2)
    tavara.paino()