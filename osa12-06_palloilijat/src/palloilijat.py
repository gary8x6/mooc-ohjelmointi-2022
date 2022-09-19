class Palloilija:
    def __init__(self, nimi: str, pelinumero: int, maalit: int, syotot: int, minuutit: int):
        self.nimi = nimi
        self.pelinumero = pelinumero
        self.maalit = maalit
        self.syotot = syotot
        self.minuutit = minuutit

    def __str__(self):
        return (f'Palloilija(nimi={self.nimi}, pelinumero={self.pelinumero}, '
            f'maalit={self.maalit}, syotot={self.syotot}, minuutit={self.minuutit})')

# TEE RATKAISUSI TÄHÄN:
def eniten_maaleja(pelaajat: list):

    lista = sorted(pelaajat, key= lambda x: x.maalit)

    return lista[-1].nimi

def eniten_pisteita(pelaajat: list):

    lista = sorted(pelaajat, key= lambda pelaaja: (pelaaja.syotot + pelaaja.maalit))

    return (lista[-1].nimi, lista[-1].pelinumero)

def vahiten_minuutteja(pelaajat: list):

    lista = sorted(pelaajat, key= lambda pelaaja: pelaaja.minuutit)

    return lista[0]