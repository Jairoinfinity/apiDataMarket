from apiConnections import ApiConnections

api = ApiConnections()

data = api.getYahooHistorical("1mo")
print(data)