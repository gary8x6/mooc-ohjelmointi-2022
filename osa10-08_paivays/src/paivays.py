# TEE RATKAISUSI TÄHÄN:
import datetime

class Paivays:

    def __init__(self, paiva: int, kuukausi: int, vuosi: int):
        self.__paiva = paiva
        self.__kuukausi = kuukausi
        self.__vuosi = vuosi

        

    def __str__(self):

        return f"{self.__paiva}.{self.__kuukausi}.{self.__vuosi}"

    @property
    def paiva(self):
        pass

    def __eq__(self, vertailu):

        return self.__paiva == vertailu.__paiva and self.__kuukausi == vertailu.__kuukausi and self.__vuosi == vertailu.__vuosi


    def __ne__(self,vertailu):

        return self.__paiva != vertailu.__paiva or self.__kuukausi != vertailu.__kuukausi or self.__vuosi != vertailu.__vuosi

    def __gt__(self,vertailu):

        return (self.__paiva + self.__kuukausi * 30 + self.__vuosi * 365) > (vertailu.__paiva + vertailu.__kuukausi * 30 + vertailu.__vuosi * 365)

    def __lt__(self,vertailu):

        return (self.__paiva + self.__kuukausi * 30 + self.__vuosi * 365) < (vertailu.__paiva + vertailu.__kuukausi * 30 + vertailu.__vuosi * 365)

    def __add__(self, lisäys):

        paivina = self.__paiva + self.__kuukausi * 30 + self.__vuosi * 360

        paivina += lisäys

        vuodet = paivina / 360
        kuukaudet = paivina % 360
        paivat = kuukaudet % 30
        kuukaudet = kuukaudet / 30


        uusi_paiva = Paivays(int(paivat), int(kuukaudet), int(vuodet))


        return uusi_paiva


    def __sub__(self,vertailu):

        paivina = self.__paiva + self.__kuukausi * 30 + self.__vuosi * 360
        vertailu = vertailu.__paiva + vertailu.__kuukausi * 30 + vertailu.__vuosi * 360


        return abs(vertailu - paivina)

if __name__ == "__main__":
    p1 = Paivays(4, 10, 2020)
    p2 = Paivays(28, 12, 1985)

    p3 = p1 + 3
    p4 = p2 + 400

    print(p1)
    print(p2)
    print(p3)
    print(p4)
