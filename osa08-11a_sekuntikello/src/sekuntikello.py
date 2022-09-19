# Tee ratkaisusi tähän:
class Sekuntikello:
    def __init__(self):
        self.sekunnit = 0
        self.minuutit = 0

    def __str__(self):

        sekunnit = str(self.sekunnit)
        minuutit = str(self.minuutit)

        if len(sekunnit) == 1:
            sekunnit = "0"+sekunnit

        if len(minuutit) == 1:
            minuutit = "0"+minuutit

        return f"{minuutit}:{sekunnit}"

    def tick(self):

        if self.sekunnit < 59:
            self.sekunnit += 1
        else:
            self.minuutit += 1
            self.sekunnit = 0

        if self.minuutit > 59:
            self.minuutit = 0

if __name__ == "__main__":   

    kello = Sekuntikello()

    for i in range(3600):
        print(kello)
        kello.tick() 
