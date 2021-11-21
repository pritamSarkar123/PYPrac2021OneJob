import pandas as pd 
import sqlalchemy 
from binance.client import Client
from binance import BinanceSocketManager
from dotenv import load_dotenv
import os
import asyncio
import sys

print('PYTHON PID:', os.getpid(), flush=True)
kill_cmd = '''taskkill /F /PID ''' + str(os.getpid())
print('EMERGENCY KILL COMMAND:', kill_cmd, flush=True)


load_dotenv()

def createframe(msg):
    df = pd.DataFrame([msg])
    df = df.loc[:,['s','E','p']]
    df.columns = ['symbol','Time','Price']
    df.Price = df.Price.astype(float)
    df.Time = pd.to_datetime(df.Time,unit='ms')
    return df


async def populate(coin):
    api_key = os.getenv('API_KEY')
    api_secret = os.getenv('API_SECRET')
    client = Client(api_key=api_key,api_secret=api_secret)
    bsm = BinanceSocketManager(client)
    socket = bsm.trade_socket(coin)
    engine = sqlalchemy.create_engine(f'sqlite:///databases/{coin}stream.db')
    
    while True:
        _ = await socket.__aenter__()
        msg = await socket.recv()
        frame = createframe(msg)
        frame.to_sql(coin,engine,if_exists='append',index=False)
        print(frame)
    
def main(coin):
    asyncio.run(populate(coin))

if __name__=="__main__":
    coin = sys.argv[1]
    with open(f"{coin}end.bat","w") as bat:
        bat.write(kill_cmd)
    main(coin)
    