import requests, json
from googlefinance import getQuotes
import yfinance as yf
import pandas as pd

class ApiConnections:

    # Atributos
    __YAHOO_SHARE = ""
    __GOOGLE_SHARE = ""
    __MULTIPLE_SHARE = []
    __SHARE = ""

    # Constructor
    def __init__(self):
        self.__YAHOO_SHARE = yf.Ticker("MSFT")
        self.__GOOGLE_SHARE = "AAPL"
        self.__MULTIPLE_SHARE = ["SPY", "AAPL", "MSFT"]
        self.__SHARE = "MSFT"
        print("Constructor en desarrollo")

    # Funciones Getters
    def getYahooShare(self):
        return self.__SHARE
    
    def getGoogleShare(self):
        return self.__GOOGLE_SHARE

    def getShareMultiple(self):
        return self.__MULTIPLE_SHARE
    
    # Funciones Setters
    def setYahooShare(self, share):
        self.__YAHOO_SHARE = yf.Ticker(share)
        self.__SHARE = share
        print(f"Configuración cambiada correctamente a {self.__SHARE}")
    
    def setGoogleShare(self, share):
        self.__GOOGLE_SHARE = share
        print(f"Configuración cambiada correctamente a {self.__GOOGLE_SHARE}")
    
    def setShareMultiple(self, shares):
        self.__MULTIPLE_SHARE = shares
        print(f"Configuración cambiada correctamente a {self.__MULTIPLE_SHARE}")
    

    # Funciones
    """
    getYahooHistorical() Devuelve los precios del activo en el periodo que
    se les pase por parametros.

    # period: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
    """

    def getYahooHistorical(self, period):
        data = self.__YAHOO_SHARE.history(period=period)

        jsonData = {
            "share":self.__SHARE,
            "price":[]
        }
        price = []

        for priceData in data["Close"]:
            price.append(priceData)
        
        jsonData["price"] = price
        
        return jsonData
    
    """
    getGoogleData() Devuelve los precios del activo en el periodo que
    se les pase por parametros.

    # period: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
    """
    def getGoogleData(self):
        return json.dumps(getQuotes(self.__GOOGLE_SHARE), indent=2)

    """
    getMultipleHistorical() Devuelve los precios de los activos en el periodo que
    se les pase por parametros.

    # period: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
    """
    def getMultipleHistorical(self, period):
        data = []

        for share in self.__MULTIPLE_SHARE:
            self.setYahooShare(share)
            data.append(self.getYahooHistorical(period))
        
        return data

