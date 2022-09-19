# TEE RATKAISUSI TÄHÄN:
class Lahja:
    def __init__(self, nimi: str, paino: int):
        self.nimi = nimi
        self.paino = paino

    def __str__(self):
        return f"Lahja: {self.nimi} (2 kg)"


class Pakkaus:
    def __init__(self):
        self.lahjat = []

    def lisaa_lahja(self, lahja: "Lahja"):

        self.lahjat.append(lahja)

    def yhteispaino(self):

        paino = 0

        for lahja in self.lahjat:

            paino += lahja.paino

        return paino
