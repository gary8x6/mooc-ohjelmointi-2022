# TEE RATKAISUSI TÄHÄN:

class Asunto:
    def __init__(self, huoneita: int, nelioita: int, neliohinta: int):
        self.huoneita = huoneita
        self.nelioita = nelioita
        self.neliohinta = neliohinta

    def suurempi(self, verrattava: "Asunto"):
        return self.nelioita > verrattava.nelioita

    def hintaero(self, verrattava: "Asunto"):
        return abs(self.nelioita*self.neliohinta - verrattava.nelioita*verrattava.neliohinta)

    def kalliimpi(self, verrattava: "Asunto"):
        return (self.nelioita*self.neliohinta) > (verrattava.nelioita*verrattava.neliohinta)

