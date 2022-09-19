# TEE RATKAISUSI TÄHÄN:

class Pankkitili:

    def __init__(self, omistaja: str, tilinumero: str, saldo: float):

        self.__omistaja = omistaja
        self.__tilinumero = tilinumero
        self.__saldo = saldo

    def __palvelumaksu(self):

        self.__saldo -= (self.__saldo * 0.01)


    def talleta(self, summa: float):
        if summa > 0:

            self.__saldo += summa
            self.__palvelumaksu()

        else:

            pass


    def nosta(self, summa: float):

        if self.__saldo >= summa:
            
            self.__saldo -= summa
            self.__palvelumaksu()

        else:

            pass

    @property
    def saldo(self):

        return self.__saldo
