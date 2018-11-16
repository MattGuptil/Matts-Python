from flash import Flask, jsonify

app = Flask(__name__)

@app.rout("/hello/<name>", methods = ["GET"])
def hello():
	return {"name": "{}".format(name)}

if __name__ == '__main__':
	app.run(host="127.0.0.1")
# to let others in...   app.run(host ="0.0.0.0")