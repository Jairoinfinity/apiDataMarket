import requests, json
from yahoo_finance import Share, Currency
import yfinance as yf
import pandas as pd

class ApiConnections:

    # Atributos
    __YAHOO_SHARE = "" # Acciones
    __SHARE = ""

    # Constructor
    def __init__(self):
        self.__YAHOO_SHARE = yf.Ticker("MSFT")
        self.__SHARE = "MSFT"
        print("Constructor en desarrollo")

    # Funciones Getters
    def getYahooShare(self):
        return self.__SHARE
    
    # Funciones Setters
    def setYahooShare(self, share):
        self.__YAHOO_SHARE = yf.Ticker(share)
        self.__SHARE = share
        print(f"Configuración cambiada correctamente a {self.__SHARE}")
    

    # Funciones
    """
    getYahooHistorical() Devuelve los precios de del activo en el rango de fechas que
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
