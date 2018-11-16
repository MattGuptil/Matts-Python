







import requests
if __name__ == '__main__':
	
	myval = 'string'
	while(True):
		r2 = requests.post("127.0.0.1:5000", json={
	  	
 		"a": [2, 4],
  		"b": [5, 6]


		})
