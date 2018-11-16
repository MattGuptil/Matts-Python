







import requests
if __name__ == '__main__':
	
	r2 = requests.post("http://127.0.0.1:5000/sum", json={"a": [2, 4], "b": [5, 6]})
