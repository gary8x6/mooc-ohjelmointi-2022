# TEE RATKAISUSI TÄHÄN:
class Tietokonepeli:
    def __init__(self, nimi: str, julkaisija: str, vuosi: int):
        self.nimi = nimi
        self.julkaisija = julkaisija
        self.vuosi = vuosi

class Pelivarasto:
    def __init__(self):
        self.__pelit = []

    def lisaa_peli(self, peli: Tietokonepeli):
        self.__pelit.append(peli)

    def anna_pelit(self):
        return self.__pelit

class Pelimuseo(Pelivarasto):

    def __init__(self):
        super().__init__()

    def anna_pelit(self):
        
        games = []

        for peli in super().anna_pelit():
            if peli.vuosi < 1990:
                games.append(peli)

        return games


