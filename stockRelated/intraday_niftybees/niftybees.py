import sqlalchemy
import pandas as pd
import yfinance as yf
import os
import sys
engine = None

def create_engine(name,path=""):
    global engine 
    engine = sqlalchemy.create_engine(f'sqlite:///{os.path.join(path,name)}.db')
    print("DB engine created .........................................")
    

def get_all_current_data(name,ticker,interval='1d',period='20y',path=""):
    global engine
    try:
        data = yf.download(ticker,period=period,interval=interval,start=None,end=None).reset_index()
        data.to_sql(ticker,engine,index=False,if_exists='replace')
        print("data download succesful ...............................")
    except:
        print("data download not possible due to some error .......................-_-")
        

def load_data_to_dataframe(name,ticker,path=""):
    global engine
    data = pd.read_sql(ticker,engine)
    return data

def create_model(x_train):
    ####MODEL cretion #####
    model = Sequential()  # define the Keras model
    model.add(
        LSTM(units=240, return_sequences=True, input_shape=(x_train.shape[1], 6)))  # 120 neurons in the hidden layer
    ##return_sequences=True makes LSTM layer to return the full history including outputs at all times
    model.add(Dropout(0.2))
    model.add(LSTM(units=520, return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(units=520, return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(units=128, return_sequences=False))
    model.add(Dropout(0.2))
    model.add(Dense(units=1, activation='sigmoid'))
    # adding optimizer and loss function
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model


if __name__ =="__main__":
    create_engine(name="NIFTYBEES",path="databases")
    get_all_current_data(name="NIFTYBEES",ticker="NIFTYBEES.NS",interval='1d',period='20y',path="databases")
    df = load_data_to_dataframe(name="NIFTYBEES",ticker="NIFTYBEES.NS",path="databases")
    
    