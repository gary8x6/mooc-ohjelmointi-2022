# Tee ratkaisusi tähän:
class Kirja:

    def __init__(self, nimi: str, kirjoittaja: str, genre: str, kirjoitusvuosi: int):

        self.kirjoittaja = kirjoittaja
        self.nimi = nimi
        self.genre = genre
        self.kirjoitusvuosi = kirjoitusvuosi

    def __str__(self) -> str:
        return f"{self.kirjoittaja}: {self.nimi} ({self.kirjoitusvuosi})"