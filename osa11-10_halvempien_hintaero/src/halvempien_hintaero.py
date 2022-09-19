class Asunto:
    def __init__(self, huoneita: int, nelioita: int, neliohinta:int, kuvaus: str):
        self.huoneita = huoneita
        self.nelioita = nelioita
        self.neliohinta = neliohinta
        self.kuvaus = kuvaus

    def suurempi(self, verrattava):
        return self.nelioita > verrattava.nelioita

    def hintaero(self, verrattava):
        # Funktio abs palauttaa itseisarvon
        ero = abs((self.neliohinta * self.nelioita) - (verrattava.neliohinta * verrattava.nelioita))
        return ero

    def kalliimpi(self, verrattava):
        ero = (self.neliohinta * self.nelioita) - (verrattava.neliohinta * verrattava.nelioita)
        return ero > 0

    def __repr__(self):
        return (f'Asunto(huoneita = {self.huoneita}, nelioita = {self.nelioita}, ' + 
            f'neliohinta = {self.neliohinta}, kuvaus = {self.kuvaus})')

# TEE RATKAISUSI TÄHÄN:
def halvemmat(asunnot: list, verrattava: Asunto):

    return [(asunto, asunto.hintaero(verrattava)) for asunto in asunnot if not asunto.kalliimpi(verrattava) and asunto.hintaero(verrattava) > 0]

if __name__ == "__main__":
    a1 = Asunto(1, 16, 5500, "Eira yksiö")
    a2 = Asunto(2, 38, 4200, "Kallio kaksio")
    a3 = Asunto(3, 78, 2500, "Jakomäki kolmio")
    a4 = Asunto(6, 215, 500, "Suomussalmi omakotitalo")
    a5 = Asunto(4, 105, 1700, "Kerava 4h ja keittiö")
    a6 = Asunto(25, 1200, 2500, "Haikon kartano")

    a7 = Asunto(1,1,1,"a")
    a8 = Asunto(1,1,2,"b")

    asunnot2 = [a7]

    asunnot = [a1, a2, a3, a4, a5, a6]
    print(halvemmat(asunnot2, a8))