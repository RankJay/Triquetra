import requests
import io


def RaribleFetchingSchema(itemId):
    urlMeta = "http://api.rarible.com/protocol/v0.1/ethereum/nft/items/" + itemId + "/meta"
    urlInfo = "http://api.rarible.com/protocol/v0.1/ethereum/nft/items/" + itemId

    queryString = {"itemId": itemId}

    response = requests.request("GET", urlMeta, params=queryString)
    creatorResponse =  requests.request("GET", urlInfo, params=queryString)
    fname = "./scripts/RaribleOutput.json"

    with io.open(fname, "w", encoding="utf-8") as f:
        writer = creatorResponse.text
        f.write(writer)
        f.close()

    imageUrl = response.json()['properties']['image']
    creator = creatorResponse.json()['creator']
    currentOwner = creatorResponse.json()['owners'][0]
    if "ipfs://" in response.json()['properties']['image']:
        imageUrl = response.json()['properties']['image'].replace("ipfs://", "https://ipfs.io/")

    print(imageUrl)


# RaribleFetchingSchema("0xd07dc4262bcdbf85190c01c996b4c06a461d2430:0x000000000000000000000000000000000000000000000000000000000006fcc8")