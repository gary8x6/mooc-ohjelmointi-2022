# tee ratkaisu tänne

def rivien_summat(matriisi:list):

    i = 0
    summa = 0

    for rivi in matriisi:
        for numero in rivi:
            summa += numero
            
        print(summa)
        matriisi[i].append(summa)
        i += 1
        summa = 0



if __name__ == "__main__":

    matriisi = [[1,2],[3,4]]

    rivien_summat(matriisi)

    print(matriisi)