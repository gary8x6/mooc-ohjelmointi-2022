# TEE RATKAISUSI TÄHÄN:
def summa(luku: int):

    if luku <= 1:
        return luku

    return luku + summa(luku - 1)


if __name__ == "__main__":

    print(summa(2))