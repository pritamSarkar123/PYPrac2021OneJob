import os 
import subprocess
import sys
import time
import pandas as pd
import sqlalchemy 
from binance.client import Client
from binance import BinanceSocketManager
from dotenv import load_dotenv

print('PYTHON PID:', os.getpid(), flush=True)
kill_cmd = '''taskkill /F /PID ''' + str(os.getpid())
print('EMERGENCY KILL COMMAND:', kill_cmd, flush=True)

load_dotenv()

def strategy(coin,entry,lookback,qty,open_position=False):
    api_key = os.getenv('API_KEY')
    api_secret = os.getenv('API_SECRET')
    client = Client(api_key=api_key,api_secret=api_secret)
    bsm = BinanceSocketManager(client)
    socket = bsm.trade_socket(coin)
    engine = sqlalchemy.create_engine(f'sqlite:///databases/{coin}stream.db')
    
    while True:
        df = pd.read_sql(coin,engine)
        lookbackperiod = df[-lookback:]
        cumret = (lookbackperiod.Price.pct_change()+1).cumprod()-1
        if not open_position:
            if cumret[cumret.last_valid_index()] > entry:
                order = client.order(symbol=coin,
                                     side='BUY',
                                     type='MARKET',
                                     quantity=qty)
                print(order)
                open_position = True 
                break
    if open_position:
        while True:
            df = pd.read_sql(coin,engine)
            sincebuy = df.loc[df.Time > pd.to_datetime(order['transactTime'],unit='ms')]
            if len(sincebuy) > 1:
                sincebuyret = (sincebuy.Price.pct_change()+1).cumprod()-1
                last_entry = sincebuyret[sincebuyret.last_valid_index()]
                if last_entry > 0.0015 or last_entry < -0.0015:
                    order = client.order(symbol=coin,
                                     side='SELL',
                                     type='MARKET',
                                     quantity=qty)
                    print(order)
                    break 


if __name__=="__main__":
    coin = sys.argv[1]
    entry = float(sys.argv[2]) 
    lookback = int(sys.argv[3])
    qty = float(sys.argv[4]) 
    
    print("process 2 finishes")

    # TODO -_-
    # TODO this block will not be placed here
    time.sleep(40)
    # TODO this block will not be placed here
    
    #strategy(coin=coin,entry=entry,lookback=lookback,qty=qty) #lookback in sec
    # strategy(0.001,60,0.001) #60 sec
    subprocess.call([f'{coin}end.bat'])
    os.remove(f'{coin}end.bat')
    command = "python clean_database.py"
    command += " " +coin 
    os.system(command)
    
    
    