# TEE RATKAISUSI TÄHÄN:
def jarjesta_tuotantokausien_mukaan(alkiot: list):

    def jarjesta_kausien_maaran_mukaan(sanakirja: dict):
        
        return sanakirja["kausia"]

    return sorted(alkiot, key= jarjesta_kausien_maaran_mukaan)