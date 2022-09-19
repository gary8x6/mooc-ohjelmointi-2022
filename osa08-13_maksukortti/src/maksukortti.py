# Tee ratkaisusi tähän:
from turtle import Vec2D


class Maksukortti:
    def __init__(self, alkusaldo: float):

        self.saldo = alkusaldo

    def __str__(self):

        return f"Kortilla on rahaa {self.saldo:.1f} euroa"

    def syo_edullisesti(self):

        if self.saldo >= 2.6:

            self.saldo -= 2.6


    def syo_maukkaasti(self):

        if self.saldo >= 4.6:

            self.saldo -= 4.6

    def lataa_rahaa(self, lataa: float):

        if lataa < 0:
            raise ValueError
        else:
            self.saldo += lataa




pekan_kortti = Maksukortti(20)
matin_kortti = Maksukortti(30)

pekan_kortti.syo_maukkaasti()
matin_kortti.syo_edullisesti()

print("Pekka: " + str(pekan_kortti))
print("Matti: " + str(matin_kortti))

pekan_kortti.lataa_rahaa(20)
matin_kortti.syo_maukkaasti()

print("Pekka: " + str(pekan_kortti))
print("Matti: " + str(matin_kortti))

pekan_kortti.syo_edullisesti()
pekan_kortti.syo_edullisesti()

matin_kortti.lataa_rahaa(50)

print("Pekka: " + str(pekan_kortti))
print("Matti: " + str(matin_kortti))






