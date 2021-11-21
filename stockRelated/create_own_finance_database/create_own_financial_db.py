import sqlalchemy
import pandas as pd
import yfinance as yf
import os
import sys

def get_tickers(region):
    wiki = 'https://en.wikipedia.org/wiki/'
    return pd.read_html(wiki+region)[1].Symbol.to_list()


def getdata(tickers,period,interval):
    ''' Downloads data '''
    return (yf.download(ticker,period=period,interval=interval,start=None,end=None).reset_index() for ticker in tickers)


def createengine(name,path=""):
    ''' Returns a database engine'''
    return sqlalchemy.create_engine(f'sqlite:///{os.path.join(path,name)}')



def TOSQL(frames,symbols,engine):
    ''' Stores the imported data in database'''
    for frame,symbol in zip(frames,symbols):
        frame.to_sql(symbol,engine,index=False,if_exists='replace')
    print(f'Succesfully imported data ...')


def get_and_store_data(name,ticker_source,period="1mo",interval='1m',path=""):
    ''' Handles each country s'''
    try:
        tickers = get_tickers(ticker_source)
        country_data = getdata(tickers,period,interval)
        engine = createengine(name,path)
        TOSQL(country_data,tickers,engine)
        return 1
    except BaseException:
        return 0
    

ticker_sources = {"india":"BSE_SENSEX","usa":"Dow_Jones_Industrial_Average"}
 
def main(countries,periods,intervals):
    path = "databases"
    output = [get_and_store_data(countries[index],ticker_sources[countries[index]],period=periods[index],interval=intervals[index],path=path) for index in range(len(countries))]
    print(output)

if __name__=="__main__":
    #default = '1mo'# valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
    #default = '1d' # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
    #one day interval data required 1d
    countries = []
    periods = []
    intervals = []
    
    for i in range(1,len(sys.argv)):
        smaller = sys.argv[i]
        if smaller in ticker_sources:
            countries.append(smaller)
            periods.append('1mo')
            intervals.append('1d')
        else:
            print(f"{smaller} is ignored as relevant stock map not present")
    main(countries,periods,intervals)
    
    