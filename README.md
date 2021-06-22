# Requirements :
* web3
* pandas
* requests
* json
* multiprocessing

# How to run the code :
* clone the repo and extract the file
* execute `main.py` or `quickMain.py`

You should get all trades in UNI/ETH pair swaps in UNISWAP for the past one week, stored in a `output.csv` file.

# Files Description :
* `main.py` - executes the entire program
* `block.py` - connects to an Ethereum node to retrieve latest block number and calculates block number one week ago
* `query.py` - querying theGraph for UNISWAP UNI/ETH swaps based on latest block number
* `calc.py` - reads each swap data and provides output : order-type and no. of UNI per ETH
* `quickMain.py` - since connecting to ethereum chain is time consuming , run based on a predetermined block number
* `swaps.csv` - store all swaps queried from theGraph 
* `output.csv` - store output in clean format

# `output.csv` description
1. `timestamp` - Time stamp of the Swap
1. `order type` - Is it a BUY or SELL order
1. `eth` - Amount of ETH involved in the transaction
1. `uni` - Amount of UNI tokens involved in the transaction
1. `uni/eth` - Price of UNI token in ETH
1. `usd volume` - USD equivalent volume of the Swap
1. `transaction.id` - Transaction hash of the Swap
1. `block number` - Block number where the transaction is included