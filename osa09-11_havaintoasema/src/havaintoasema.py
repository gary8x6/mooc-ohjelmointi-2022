# TEE RATKAISUSI TÄHÄN:

class Havaintoasema:

    def __init__(self, nimi: str):

        self.__nimi = nimi
        self.__havainnot = []

    def __str__(self):

        return f"{self.__nimi}, {len(self.__havainnot)} havaintoa"

    def lisaa_havainto(self, havainto: str):

        self.__havainnot.append(havainto)

    def viimeisin_havainto(self):

        if len(self.__havainnot) > 0:

            return self.__havainnot[-1]

        else:

            return ""

    def havaintojen_maara(self):

        return len(self.__havainnot)

if __name__ == "__main__":

    asema = Havaintoasema("Kumpula")

    print(asema.viimeisin_havainto())

    print(asema.viimeisin_havainto())

    print(asema.havaintojen_maara())
    print(asema)