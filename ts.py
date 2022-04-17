import requests, json

data = requests.get(url='http://192.168.227.67:8000/api/qs-history/all/').text

# data = (type(json.loads(data)))
data = json.loads(data)
data = data[::-1]
print(data)
