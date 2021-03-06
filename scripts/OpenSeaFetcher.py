import requests
import io


def OpenSeaFetchingSchema(token_id_of_nft, asset_contract_address_of_nft):
    print(token_id_of_nft, asset_contract_address_of_nft)
    url = "https://api.opensea.io/api/v1/assets"

    queryString = {"token_ids":token_id_of_nft, "asset_contract_address":asset_contract_address_of_nft, "limit":"1"}

    response = requests.request("GET", url, params=queryString)
    fname = "./scripts/OpenSeaOutput.json"

    with io.open(fname, "w", encoding="utf-8") as f:
        writer = response.text
        writer.replace("'", '"')
        writer.replace("True", '"True"')
        writer.replace("False", '"False"')
        f.write(writer)
        f.close()

    # print( response.json()['assets'][0]['name'], response.json()['assets'][0]['description'], response.json()['assets'][0]['asset_contract']['schema_name'], response.json()['assets'][0]['permalink'], response.json()['assets'][0]['collection']['twitter_username'] )

    return response.json()['assets'][0]['name'], response.json()['assets'][0]['permalink']

# OpenSeaFetchingSchema("40930059826298205183487168041223830856677554863973398691462482759410010554369", "0x495f947276749ce646f68ac8c248420045cb7b5e")