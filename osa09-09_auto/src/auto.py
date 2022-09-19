# TEE RATKAISUSI TÄHÄN:

class Auto:

    def __init__(self):

        self.__tankki = 0
        self.__mittari = 0

    def __str__(self):

        return f"Auto: ajettu {self.__mittari} km, bensaa {self.__tankki} litraa"

    def tankkaa(self):
        
        self.__tankki = 60
        

    def aja(self, km: int):

        if self.__tankki >= km:

            self.__mittari += km
            self.__tankki -= km

        elif self.__tankki < km:

            self.__mittari += self.__tankki
            self.__tankki = 0
