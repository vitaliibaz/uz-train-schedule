import requests

def data_find(address):
	return requests.get(address).text


# test
print(data_find('https://api.github.com/meta'))
