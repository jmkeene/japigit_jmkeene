import sys
import pandas as pd
import urllib.request
import json
from alpha_vantage.timeseries import TimeSeries
#justin keene
#IFT458
API_KEY = 'PE6SJ7PGCKYS6F5J'
def getStockdata(symbol):

    try:
        #------ failed use of urllib -------
        #queryUrl = "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol="+symbol+"&apikey=PE6SJ7PGCKYS6F5J"
        #connection = urllib.request.urlopen(queryUrl)
        #responseString = connection.read().decode()
        #json_str = json_loads(responseString)
        #return str(responseString.globalquote.price)
        #return str(responseString)
        timeSeries = TimeSeries(key=API_KEY, output_format='pandas')
        data, meta_data = timeSeries.get_intraday(symbol=symbol, interval='1min')
        return str(data.tail(1).iloc[0]['4. close'])
    except:
        return "not found"

def main():
    outFile = open('japi.out', 'w')

    while 1:
        userInput = input("Enter Stock Symbol or EXIT to exit: ").upper()
        if userInput != "EXIT":
            serverData = 'The current price of {} is {}\n'.format(userInput, getStockdata(userInput))
            print(serverData)
	    print("Stock Quotes retrieved successfully")
            outFile.write(serverData)
        else:
            sys.exit("\nExiting Program\n")
main()
