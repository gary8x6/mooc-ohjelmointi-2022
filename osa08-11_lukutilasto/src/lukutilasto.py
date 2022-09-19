# Tee ratkaisusi tähän:
class  Lukutilasto:
    def __init__(self):
        self.lukuja = []

    def lisaa_luku(self, luku:int):

        if luku == -1:
            return False
        else:
            self.lukuja.append(luku)
            return True

    def lukujen_maara(self):

        return len(self.lukuja)

    def summa(self):

        summat = 0

        for luku in self.lukuja:
            summat += luku

        return summat


    def keskiarvo(self):

        if len(self.lukuja) > 0:

            summat = 0

            for luku in self.lukuja:
                summat += luku

            return (summat/len(self.lukuja))

print("Anna lukuja:")
tilasto = Lukutilasto()
parillinen = Lukutilasto()
pariton = Lukutilasto()
running = True

while running == True:

    luku = input()
    luku = int(luku)

    running = tilasto.lisaa_luku(luku)

    if luku % 2 == 0 and luku != -1:

        parillinen.lisaa_luku(luku)

    else:

        pariton.lisaa_luku(luku)

print("Lukujen määrä:", tilasto.lukujen_maara())
print("Summa:", tilasto.summa())
print("Keskiarvo:", tilasto.keskiarvo())
print("Parillisten summa:", parillinen.summa())
print("Parittomien summa:", pariton.summa())
