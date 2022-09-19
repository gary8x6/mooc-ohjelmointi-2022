# TEE RATKAISUSI TÄHÄN:
class Lottorivi:

    def __init__(self, kierros, oikearivi):

        self.kierros = kierros
        self.oikearivi = oikearivi

    def osumien_maara(self, pelattu_rivi: list):
        return len([numero for numero in pelattu_rivi if numero in self.oikearivi])

    def osumat_paikoillaan(self, pelattu_rivi: list):
        return [numero if numero in self.oikearivi else -1 for numero in pelattu_rivi]