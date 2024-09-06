import yfinance as yf
import pandas as pd

def readDataFromYahoo(ticker, startDate, endDate):
    stocks = yf.Ticker(ticker)
    stockData = stocks.history(start = startDate , end = endDate)
    return stockData

def readDataFromFile(fileName):
    price = pd.read_csv('DataFileFolder\\' + fileName, index_col = 'Date' , parse_dates = True)
    return price

def saveDataToCsv(stockData, stockName):
    # startDate = stockData.index.min()
    # endDate = stockData.index.max()    
    fileName = 'price_'+ stockName + '.csv'
    directory = 'DataFileFolder\\'+ fileName
    stockData.to_csv(directory)
    return fileName
    
def toReturns():
    # Todo
    return 0

def toLogReturns():
    # Todo
    return 0

















