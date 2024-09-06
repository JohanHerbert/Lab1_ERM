import yfinance as yf

def readDataFromYahoo(ticker, startDate, endDate):
    stocks = yf.Ticker(ticker)
    stockData = stocks.history(start = startDate , end = endDate)
    return stockData

def readDataFromFile():
    # Todo
    return 0

def saveDataToCsv(stockData, filename, stockName):
    startDate = stockData.index.min()
    endDate = stockData.index.max()    

    stockData.to_csv('DataFileFolder\\' + 'price_'+ stockName + f'_{startDate}'+ f'_{endDate}'+'.csv', index=False)
    # filepath = 'C:\\ ..\\'
# price.to_csv(filepath + 'apple_price_data.csv')
    
    # Todo
    return 0

def toReturns():
    # Todo
    return 0

def toLogReturns():
    # Todo
    return 0

















