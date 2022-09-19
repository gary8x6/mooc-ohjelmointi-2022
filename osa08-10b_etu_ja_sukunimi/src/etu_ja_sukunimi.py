# Tee ratkaisusi tähän:
class Henkilo:
    def __init__(self, nimi: str):

        self.nimi = nimi

    def anna_etunimi(self):

        return self.nimi.split(" ", 1)[0]

    def anna_sukunimi(self):

        return self.nimi.split(" ", 1)[1]













