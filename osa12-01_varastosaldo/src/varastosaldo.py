# TEE RATKAISUSI TÄHÄN:
def jarjesta_varastosaldon_mukaan(alkiot: list):

    def jarjestys(alkio: tuple):
        return alkio[2]

    return sorted(alkiot, key=jarjestys)