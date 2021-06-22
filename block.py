from web3 import Web3

currentBlock = 0

lastWeekBlock = 0


def blockNum():
    secsInWeek = 604800
    oneBlock = 12
    blockHis = secsInWeek/oneBlock

    eth = 'https://mainnet.infura.io/v3/3053033d662142a38e4751da855e1d98'
    web3 = Web3(Web3.HTTPProvider(eth))

    if(web3.isConnected()):
        print("connected")
    else:
        print('not connected')
        exit()

    currentBlock = web3.eth.block_number

    lastWeekBlock = int(currentBlock-blockHis)

    return { "current" : currentBlock, "lastWeek" : lastWeekBlock }


