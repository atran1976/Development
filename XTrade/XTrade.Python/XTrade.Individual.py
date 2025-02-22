
from ast import arg
from calendar import c
from datetime import datetime
from locale import currency
from math import fabs
import profile
from numpy import mat
from yahooquery import Ticker
import threading
import pandas as pd
import sys
import math 
import requests
import time
import re


def GetInsiderTransactionsBySymbol(symbol):

    content = ["Symbol,Date,Holder,Title,Description,Shares,Value,Ownership\n"]

    tickers = Ticker(symbol)
    transactions = tickers.insider_transactions

    df = pd.DataFrame(transactions)
    df.head()

    for s, dr in df.iterrows():
        try:
            symbol = dr.name[0]
            date = dr['startDate']
            holder = dr['filerName']
            title = dr['filerRelation']
            desc = dr['transactionText']
            shares = dr['shares']
            value = dr['value']
            ownership = dr['ownership']
           
            content.append(f"{symbol.upper()},{date},{holder},{title},{desc},{shares},{value},{ownership}\n")
           
        except Exception as e:
            print(f"err on parsing summary : {s} - {e}")  

    print("".join(content));

def GetInsiderTransactionsBySymbol(symbol):

    content = ["Symbol,Date,Holder,Title,Description,Shares,Value,Ownership\n"]

    tickers = Ticker(symbol)
    transactions = tickers.insider_transactions

    df = pd.DataFrame(transactions)
    df.head()

    for s, dr in df.iterrows():
        try:
            symbol = dr.name[0]
            date = dr['startDate']
            holder = dr['filerName']
            title = dr['filerRelation']
            desc = dr['transactionText']
            shares = dr['shares']
            value = dr['value']
            ownership = dr['ownership']
           
            content.append(f"{symbol.upper()},{date},{holder},{title},{desc},{shares},{value},{ownership}\n")
           
        except Exception as e:
            print(f"err on parsing insider transactions : {s} - {e}")  


    print("".join(content))

def GetInsiderPurchaseActivityBySymbol(symbol):

    content = ["Symbol,Period,BuyCount,BuyShares,BuyPercentInsiderShares,SellCount,SellShares,SellPercentInsiderShares,NetCount,NetShares,NetPercentInsiderShares,TotalInsiderShares\n"]

    tickers = Ticker(symbol)
    transactions = tickers.share_purchase_activity

    df = pd.DataFrame(transactions)
    df.head()

    for s, dr in df.items():
        try:
            symbol = dr.name
            period = dr['period']
            buyInfoCount = dr['buyInfoCount']
            buyInfoShares = dr['buyInfoShares']
            buyPercentInsiderShares = dr['buyPercentInsiderShares']
            sellInfoCount = dr['sellInfoCount']
            sellInfoShares = dr['sellInfoShares']
            sellPercentInsiderShares = dr['sellPercentInsiderShares']
            netInfoCount = dr['netInfoCount']
            netInfoShares = dr['netInfoShares']
            netPercentInsiderShares = dr['netPercentInsiderShares']
            totalInsiderShares = dr['totalInsiderShares']
                 
            content.append(f"{symbol.upper()},{period},{buyInfoCount},{buyInfoShares},{buyPercentInsiderShares},{sellInfoCount},{sellInfoShares},{sellPercentInsiderShares},{netInfoCount},{netInfoShares},{netPercentInsiderShares},{totalInsiderShares}\n")
           
        except Exception as e:
            print(f"err on parsing insider purchase activities : {s} - {e}")  


    print("".join(content))

def GetSECFillingsBySymbol(symbol):

    content = ["Symbol,Date,Type,Title,Url\n"]
 
    ticker = Ticker(symbol)
    transactions = ticker.sec_filings

    df = pd.DataFrame(transactions)
    df.head()

    for s, dr in df.iterrows():
        try:
            symbol = dr.name[0]
            date = dr['date']
            action = dr['type']
            title = dr['title']
            url = dr['edgarUrl']
           
            content.append(f"{symbol.upper()},{date},{action},{title},{url},\n")
           
        except Exception as e:
            print(f"err on parsing sec fillings : {s} - {e}")  


    print("".join(content))






#entry of program
if __name__ == "__main__":
    function = sys.argv[1]
    symbol = sys.argv[2]

    if function == "GetInsiderTransactionsBySymbol":
        GetInsiderTransactionsBySymbol(symbol)
    elif function == "GetInsiderPurchaseActivityBySymbol":
        GetInsiderPurchaseActivityBySymbol(symbol)
    elif function == "GetSECFillingsBySymbol":
        GetSECFillingsBySymbol(symbol)