import requests
import pandas as pd
import json
import multiprocessing as mp
#----------------------------------

import query as q
import block
import calc
#----------------------------------

# get the current block and block approximately one week before
# blocks = block.blockNum()
c = 12684280
secsInWeek = 604800
oneBlock = 12
blockHis = secsInWeek/oneBlock
l = int(c - blockHis)

# query first 1000 swaps from latest block
rJSON = q.query(c)
# extract swap data from query response
swaps = rJSON['data']['swaps']

# convert swap data to DataFrame
df = pd.json_normalize(swaps)

# extract last block number of the 1000 swaps
tempB = int(df.iloc[999,12])

out = df.copy(deep=True)

# loop to get all swaps until at least last week
while tempB > l :
    rJSON = q.query(tempB-1)
    swaps = rJSON['data']['swaps']
    t_df = pd.json_normalize(swaps)
    tempB = int(t_df.iloc[999,12])
    out = df.append(t_df)

out.to_csv('swaps.csv')
print("swaps.csv Done")

# assume WETH is base currency 

calc.main()

print("output.csv Done")
print(" Liquidity : " + out.iloc[1,8] + " UNI + " + out.iloc[1,9] + " ETH")