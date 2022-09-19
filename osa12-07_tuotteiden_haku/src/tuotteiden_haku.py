# TEE RATKAISUSI TÄHÄN:

def hae(tuotteet: list, kriteeri: callable):
    
    lista = []

    for tuote in tuotteet:
        if kriteeri(tuote):
            lista.append(tuote)

    return lista

def hinta_alle_4_euroa(tuote):
    return tuote[1] < 4



if __name__ == "__main__":
    tuotteet = [('Omena', 4.0, 3), ('Appelsiini', 5.95, 5), ('Banaani', 2.95, 10), ('Ananas', 5.5, 3)]

    for tuote in hae(tuotteet, hinta_alle_4_euroa):
        print(tuote)