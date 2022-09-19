# Tee ratkaisusi tähän:
class Lemmikki:

    def __init__(self, nimi, laji, syntymavuosi):
        self.nimi = nimi
        self.laji = laji
        self.syntymavuosi = syntymavuosi


def uusi_lemmikki(nimi: str, laji: str, syntymavuosi: int):

    return Lemmikki(nimi, laji, syntymavuosi)