import json
import requests

def query(block):
    query = """
    query trades{
    swaps(
        first:1000
        where:{
        pair: "0xd3d2e2692501a5c9ca623199d38826e513033a17"},
        orderBy: timestamp,
        orderDirection: desc,
        block: {number:"""+str(block)+"""}) {
        id
        timestamp
        amountUSD
        amount0In
        amount1In
        amount0Out
        amount1Out
        pair {
        id
        token0 {
            symbol
        }
        token1 {
            symbol
        }
        reserve0
        reserve1
        }
        transaction {
        id
        blockNumber
        }
    }
    }"""

        
    api = 'https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2'

    r = requests.post(api, json={'query': query})

    return r.json()
