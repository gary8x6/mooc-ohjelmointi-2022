# TEE RATKAISUSI TÄHÄN:

class Maksukortti:
    def __init__(self, saldo: float):
        self.saldo = saldo

    def lataa_rahaa(self, lisays: float):
        self.saldo += lisays

    def ota_rahaa(self, maara: float):
        if self.saldo >= maara:
            self.saldo -= maara
            return True

        return False
        # Toteuta metodi siten, että se ottaa kortilta rahaa vain, jos saldoa riittää
        # Onnistuessaan metodi palauttaa True ja muuten False

class Kassapaate:
    def __init__(self):
        # kassassa on aluksi 1000 euroa rahaa
        self.rahaa = 1000
        self.edulliset = 0
        self.maukkaat = 0

    def syo_edullisesti(self, maksu: float):
        if maksu >= 2.50:

            self.rahaa += 2.50
            self.edulliset += 1

            return maksu - 2.50

        return maksu

        # Edullinen lounas maksaa 2.50 euroa
        # Kasvatetaan kassan rahamäärää edullisen lounaan hinnalla ja palautetaan vaihtorahat
        # Jos parametrina annettu maksu ei ole riittävän suuri, ei lounasta myydä ja metodi palauttaa koko summan

    def syo_maukkaasti(self, maksu: float):
        if maksu >= 4.30:

            self.rahaa += 4.30
            self.maukkaat += 1

            return maksu - 4.30

        return maksu
        # Maukas lounas maksaa 4.30 euroa
        # Kasvatetaan kassan rahamäärää maukkaan lounaan hinnalla ja palautetaan vaihtorahat
        # Jos parametrina annettu maksu ei ole riittävän suuri, ei lounasta myydä ja metodi palauttaa koko summan

    def syo_edullisesti_kortilla(self, kortti:Maksukortti):

        if kortti.saldo >= 2.50:
            self.edulliset += 1

            return kortti.ota_rahaa(2.50)

        return kortti.ota_rahaa(2.50)
        
        # Edullinen lounas maksaa 2.50 euroa
        # Jos kortilla on tarpeeksi rahaa, vähennetään hinta kortilta ja palautetaan True
        # Muuten palautetaan False

    def syo_maukkaasti_kortilla(self, kortti:Maksukortti):

        if kortti.saldo >= 4.30:
            self.maukkaat += 1

            return kortti.ota_rahaa(4.30)

        return kortti.ota_rahaa(4.30)
        # Maukas lounas maksaa 4.30 euroa
        # Jos kortilla on tarpeeksi rahaa, vähennetään hinta kortilta ja palautetaan True
        # Muuten palautetaan False

    def lataa_rahaa_kortille(self, kortti: Maksukortti, summa: float):

        kortti.lataa_rahaa(summa)

if __name__ == "__main__":
    exactum = Kassapaate()

    vaihtorahaa = exactum.syo_edullisesti(10)
    print("Vaihtorahaa jäi", vaihtorahaa)

    vaihtorahaa = exactum.syo_edullisesti(5)
    print("Vaihtorahaa jäi", vaihtorahaa)

    vaihtorahaa = exactum.syo_maukkaasti(4.3)
    print("Vaihtorahaa jäi", vaihtorahaa)

    print("Kassassa rahaa", exactum.rahaa)
    print("Edullisia lounaita myyty", exactum.edulliset)
    print("Maukkaita lounaita myyty", exactum.maukkaat)

