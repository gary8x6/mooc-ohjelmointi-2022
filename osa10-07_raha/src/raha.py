# TEE RATKAISUSI TÄHÄN:
class Raha:
    def __init__(self, eurot: int, sentit: int):
        self.__eurot = eurot
        self.__sentit = sentit

    def __str__(self):
        return f"{self.__eurot}.{self.__sentit:02d} eur"

    def __eq__(self, toinen: int):
        return self.__eurot == toinen.__eurot and self.__sentit == toinen.__sentit

    def __lt__(self, toinen: int):
        return (self.__eurot*100 + self.__sentit) < (toinen.__eurot*100 + toinen.__sentit)

    def __gt__(self, toinen: int):
        return (self.__eurot*100 + self.__sentit) > (toinen.__eurot*100 + toinen.__sentit)

    def __ne__(self, toinen: int):
        return (self.__eurot*100 + self.__sentit) != (toinen.__eurot*100 + toinen.__sentit)

    def __add__(self, toinen: int):
        numero = ((self.__eurot*100 + self.__sentit) + (toinen.__eurot*100 + toinen.__sentit)) / 100
        return f"{numero:.2f} eur"

    def __sub__(self, toinen: int):
        if ((self.__eurot*100 + self.__sentit) - (toinen.__eurot*100 + toinen.__sentit)) >= 0:
            numero = ((self.__eurot*100 + self.__sentit) - (toinen.__eurot*100 + toinen.__sentit)) / 100
            return f"{numero:.2f} eur"
        else:
            raise ValueError(f"negatiivinen tulos ei sallittu")


if __name__ == "__main__":    
    e1 = Raha(4, 5)
    e2 = Raha(2, 95)

    e3 = e1 + e2
    e4 = e1 - e2

    print(e3)
    print(e4)

    e5 = e2-e1