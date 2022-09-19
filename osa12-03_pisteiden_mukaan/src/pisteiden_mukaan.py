# TEE RATKAISUSI TÄHÄN:
def jarjesta_pisteiden_mukaan(alkiot: list):

    def jarjesta_imdb_mukaan(sanakirja: dict):
        
        return sanakirja["pisteet"]

    return sorted(alkiot, key= jarjesta_imdb_mukaan, reverse=True)