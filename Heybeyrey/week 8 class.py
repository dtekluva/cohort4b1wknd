# working with APi
import requests
url = 'https://rest.coinapi.io/v1/assets'
headers = {'X-CoinAPI-Key' : '8B93E1CC-D792-4716-9F57-87AA9D7DD4FC'}
response = requests.get(url, headers=headers)
print(response.json())

file_name = "dataset.txt"
file = open(file_name,'w')
print(response.json(), file=file)


# Other things to take note in working with APIs: the API format = contained in the API Documentation
API call, base URL, endpoint, headers(extra authentication parameter), API key etc. URL = Base URL + endpoint url
sites 1 to get free API: expertpowerplus/API
site 2 for creating free API: jsonbin.io
