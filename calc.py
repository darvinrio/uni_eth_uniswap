import pandas as pd
import multiprocessing as mp

cpu = mp.cpu_count()

df = pd.read_csv('swaps.csv')


def calc(row):
    amt0 = row[3] # amount of uni out
    orderType = 'buy'

    eth = float(row[4])
    uni = float(row[3])

    # if amount of uni out is zero , then its a sell order
    if amt0 == 0 : 
        orderType = 'sell'
    
    if orderType == 'sell' :
        eth = float(row[5])
        uni = float(row[2])

    outDict = {
        'timestamp' : row[8],
        'order type' : orderType,
        'eth' : eth,
        'uni' : uni,
        'uni/eth' : uni/eth,
        'usd volume' : row[6],
        'transaction.id' : row[15],
        'block number' : row[14]        
    }

    return outDict


with mp.Pool(cpu) as pool :
    out = pool.map(calc, df.itertuples(name=None))

d = pd.DataFrame(out)

d.to_csv('output.csv')