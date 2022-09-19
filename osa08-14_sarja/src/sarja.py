# Tee ratkaisusi tähän:
class Sarja:
    def __init__(self, nimi: str, kaudet: int, genre: list):
        self.nimi = nimi
        self.kaudet = kaudet
        self.genre = genre
        self.arvostelut = []

    def arvostele(self, arvostelu: int):

        self.arvostelut.append(arvostelu)

    def __str__(self):



        keskiarvo = 0
        merkkijono = ", ".join(self.genre)

        if len(self.arvostelut) > 0:

            for arvo in self.arvostelut:
                keskiarvo += arvo
            
            if keskiarvo > 0:

                keskiarvo = keskiarvo / len(self.arvostelut)

            else:

                keskiarvo = 0

            return f"{self.nimi} ({self.kaudet} esityskautta) \ngenret: {merkkijono}\narvosteluja {len(self.arvostelut)}, keskiarvo {keskiarvo:.1f} pistettä"

        else:

            return f"{self.nimi} ({self.kaudet} esityskautta) \ngenret: {merkkijono}\nei arvosteluja"

    def keskiarvo(self):

        keskiarvo = 0.0

        if len(self.arvostelut) > 0:

            for arvo in self.arvostelut:
                keskiarvo += arvo

            if keskiarvo > 0:

                keskiarvo = keskiarvo / len(self.arvostelut)

            else:

                keskiarvo = 0
        
        return keskiarvo




def arvosana_vahintaan(arvosana: float, sarjat: list):
    vahintaan = []

    for sarja in sarjat:
        keskiarvo = sarja.keskiarvo()
        if keskiarvo >= arvosana:
            vahintaan.append(sarja)

    return vahintaan


def sisaltaa_genren(genre: str, sarjat: list):

    lista = []

    for sarja in sarjat:
        for gen in sarja.genre:
            if gen == genre:
                lista.append(sarja)

    return lista

if __name__ == "__main__":
    s1 = Sarja("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.arvostele(5)

    s2 = Sarja("South Park", 24, ["Animation", "Comedy"])
    s2.arvostele(3)

    s3 = Sarja("Friends", 10, ["Romance", "Comedy"])
    s3.arvostele(2)

    sarjat = [s1, s2, s3]

    print("arvosana vähintään 4.5:")
    for sarja in arvosana_vahintaan(4.5, sarjat):
        print(sarja.nimi)

    print("genre Comedy:")
    for sarja in sisaltaa_genren("Comedy", sarjat):
        print(sarja.nimi)