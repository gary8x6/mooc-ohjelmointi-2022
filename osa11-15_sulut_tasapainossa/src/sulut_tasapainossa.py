
def sulut_tasapainossa(merkkijono: str):

    sulkeet = "()[]}{"

    if len(merkkijono) == 0:
        return True

    for merkki in merkkijono:
        if merkki not in sulkeet:
            merkkijono = merkkijono.replace(merkki, "")
        
    if not (merkkijono[0] == '(' and merkkijono[-1] == ')') and not (merkkijono[0] == '[' and merkkijono[-1] == ']'):
        return False

    # poistetaan ensimmäinen ja viimeinen merkki
    return sulut_tasapainossa(merkkijono[1:-1])

if __name__ == "__main__":

    ok = sulut_tasapainossa("((a[aaa]!))")
    print(ok)