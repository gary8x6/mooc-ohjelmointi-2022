# TEE RATKAISUSI TÄHÄN:
class Henkilo:
    def __init__(self, nimi: str, pituus: int):
        self.nimi = nimi
        self.pituus = pituus

    def __str__(self):
        return self.nimi


class Huone:
    def __init__(self):
        self.henkilot = []

    def lisaa(self, henkilo: Henkilo):

        self.henkilot.append(henkilo)

    def on_tyhja(self):

        if len(self.henkilot) == 0:

            return True

        else:
            pituus = 0

            for henkilo in self.henkilot:
                pituus += henkilo.pituus

            return False


    def tulosta_tiedot(self):

        yht_pituus = 0

        for henkilo in self.henkilot:
            yht_pituus += henkilo.pituus

        print(f"Huoneessa on {len(self.henkilot)} henkilöä, yhteispituus {yht_pituus} cm")

        for henkilo in self.henkilot:
            print(f"{henkilo.nimi} ({henkilo.pituus} cm)")


    def lyhin(self):


        if len(self.henkilot) == 0:

            return None

        else:

            pituus = self.henkilot[0]

            for henkilo in self.henkilot:

                if henkilo.pituus < pituus.pituus:
                    pituus = henkilo

            return pituus

    def poista_lyhin(self):

        if self.on_tyhja() == True:
            return None

        else:

            lyhyin = self.lyhin()

            self.henkilot.remove(lyhyin)

            return lyhyin

if __name__ == "__main__":

    huone = Huone()

    huone.lisaa(Henkilo("Lea", 183))
    huone.lisaa(Henkilo("Kenya", 182))
    huone.lisaa(Henkilo("Nina", 172))
    huone.lisaa(Henkilo("Auli", 186))
    huone.tulosta_tiedot()

    print()

    poistettu = huone.poista_lyhin()
    print(f"Otettiin huoneesta {poistettu.nimi}")

    print()

    huone.tulosta_tiedot()