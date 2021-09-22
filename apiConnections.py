import requests, json
from yahoo_finance import Share, Currency

class ApiConnections:

    # Atributos
    __YAHOO_SHARE = "" # Acciones
    __YAHOO_CURRENCY = "" # Divisas

    # Constructor
    def __init__(self):
        print("Constructor en desarrollo")

    # Funciones Getters
    def getYahooShare(self):
        return self.__YAHOO_SHARE
    
    def getYahooCurrency(self):
        return self.__YAHOO_CURRENCY
    
    # Funciones Setters
    def setYahooShare(self, share):
        self.__YAHOO_SHARE = share
        print(f"Configuración cambiada correctamente a {self.__YAHOO_SHARE}")
    
    def setYahooCurrency(self, currency):
        self.__YAHOO_CURRENCY = currency
        print(f"Configuración cambiada correctamente a {self.__YAHOO_CURRENCY}")

    