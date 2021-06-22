import requests
import pandas as pd
import json
import query as q
import block
import multiprocessing as mp

cpu = mp.cpu_count()

blocks = block.blockNum()
c = blocks["current"]
l = blocks["lastWeek"]

rJSON = q.query(c)

swaps = rJSON['data']['swaps']

df = pd.json_normalize(swaps)

tempB = int(df.iloc[999,12])

out = df.copy(deep=True)

while tempB > l :
    rJSON = q.query(tempB-1)
    swaps = rJSON['data']['swaps']
    t_df = pd.json_normalize(swaps)
    tempB = int(t_df.iloc[999,12])
    out = df.append(t_df)

# assume WETH is base currency
#     



out.to_csv('swaps.csv')