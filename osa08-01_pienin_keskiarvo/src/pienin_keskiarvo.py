# tee ratkaisu tänne
def pienin_keskiarvo(henkilo1:dict, henkilo2:dict, henkilo3:dict):



    henkilo1_ka = henkilo1.get("tulos1") + henkilo1.get("tulos2") + henkilo1.get("tulos3")
    henkilo2_ka = henkilo2.get("tulos1") + henkilo2.get("tulos2") + henkilo2.get("tulos3")
    henkilo3_ka = henkilo3.get("tulos1") + henkilo3.get("tulos2") + henkilo3.get("tulos3")

    if henkilo1_ka < henkilo2_ka and henkilo1_ka < henkilo3_ka:
        return henkilo1

    elif henkilo2_ka < henkilo1_ka and henkilo2_ka < henkilo3_ka:
        return henkilo2

    elif henkilo3_ka < henkilo1_ka and henkilo3_ka < henkilo2_ka:
        return henkilo3


if __name__ == "__main__":

    henkilo1 = {"nimi": "Keijo", "tulos1": 2, "tulos2": 3, "tulos3": 3}
    henkilo2 = {"nimi": "Reijo", "tulos1": 5, "tulos2": 1, "tulos3": 8}
    henkilo3 = {"nimi": "Veijo", "tulos1": 3, "tulos2": 1, "tulos3": 1}

    print(pienin_keskiarvo(henkilo1, henkilo2, henkilo3))
