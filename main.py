from apiConnections import ApiConnections

api = ApiConnections()

api.setYahooShare("YHOO")
api.setYahooCurrency("EURUSD")
print(api.getYahooCurrency())
print(api.getYahooShare())