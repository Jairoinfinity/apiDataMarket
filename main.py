#Api V1.1
from apiConnections import ApiConnections

api = ApiConnections()

"""
Funciones de yahoo finance
"""
# data = api.getYahooHistorical("1mo")
# data = api.getMultipleHistorical("1mo")
# print(data)

"""
Funciones de google finance
"""
print(api.getGoogleData())