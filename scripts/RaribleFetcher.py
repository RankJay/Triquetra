import requests
import io


def RaribleFetchingSchema():
    url = "http://api.rarible.com/protocol/ethereum/nft/indexer/v1/items/:0x60f80121c31a0d46b5279700f9df786054aa5ee5:21/meta"

    queryString = {"@type": "by_creator", "creator": "0x5ec5957f4178cabb90865ee5564958cd5120d59c"}

    response = requests.request("GET", url)
    print(response.status_code)
    fname = "./scripts/RaribleOutput.json"

    with io.open(fname, "w", encoding="utf-8") as f:
        writer = response.text
        writer.replace("'", '"')
        writer.replace("True", '"True"')
        writer.replace("False", '"False"')
        f.write(writer)

    print(response)


RaribleFetchingSchema()