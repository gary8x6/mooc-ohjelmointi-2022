# Tee ratkaisusi tähän:
class Kello:

    def __init__(self, tunnit: int, minuutit: int, sekunnit: int):

        self.sekunnit = sekunnit
        self.minuutit = minuutit
        self.tunnit = tunnit

    def aseta(self, tunnit: int, minuutit: int):

        self.tunnit = tunnit
        self.minuutit = minuutit
        self.sekunnit = 0

    def tick(self):

        if self.sekunnit == 59:
            self.sekunnit = 0
            self.minuutit += 1
        else:
            self.sekunnit += 1

        if self.minuutit == 60:
            self.minuutit = 0
            self.tunnit += 1

        if self.tunnit == 24:
            self.tunnit = 0


    def __str__(self):

        return f"{self.tunnit:02}:{self.minuutit:02}:{self.sekunnit:02}"

if __name__ == "__main__":
        
    kello = Kello(15, 15, 15)
    kello.tick()
    print(kello)
    kello.tick()
    print(kello)
    kello.tick()
    print(kello)