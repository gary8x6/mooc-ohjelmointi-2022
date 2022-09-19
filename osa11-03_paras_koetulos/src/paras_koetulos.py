# TEE RATKAISUSI TÄHÄN:
class Koesuoritus:
    def __init__(self, nimi: str, arvosana1: int, arvosana2: int, arvosana3: int):
        self.nimi = nimi
        self.arvosana1 = arvosana1
        self.arvosana2 = arvosana2
        self.arvosana3 = arvosana3

    def __str__(self):
        return (f'Nimi:{self.nimi}, arvosana1: {self.arvosana1}' +
            f', arvosana2: {self.arvosana2}, arvosana3: {self.arvosana3}')

    def paras(self):

        lista = [self.arvosana1, self.arvosana2, self.arvosana3]

        return max(lista)


def parhaat_tulokset(suoritukset: list):

    return [suoritus.paras() for suoritus in suoritukset]
