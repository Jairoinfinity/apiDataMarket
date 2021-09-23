from apiConnections import ApiConnections

api = ApiConnections()

# data = api.getYahooHistorical("1mo")
data = api.getMultipleHistorical("1mo")
print(data)