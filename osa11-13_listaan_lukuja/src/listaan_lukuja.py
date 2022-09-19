# TEE RATKAISUSI TÄHÄN:
def listaan_lukuja(luvut: list):
       
    while (len(luvut) % 5) != 0:
        luvut.append(luvut[-1] + 1)
        listaan_lukuja(luvut) 


    



if __name__ == "__main__":

    listaan_lukuja([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110])