from flask import Flask, jsonify, request
import requests
import json
import numpy as np
app = Flask(__name__)

@app.route("/name", methods = ["GET"])
def name():
	return jsonify({"name": "<your name here>"}), 200


@app.route("/hello/<name>", methods = ["GET"])
def hello(name):
	myd = {
	"message": "Hello there, {}".format(name)
	}
	return jsonify(myd), 200


@app.route("/sum", methods=["POST"])
def sum():
  r = request.get_json() # parses the POST request body as JSON
  s = np.sqrt(r["a"][0]**2  - r["b"][0]**2) # adds JSON dict parameter "a" and "b" together
  mydict = {"distance": s, "a": r["a"]}
  return jsonify(mydict), 200

if __name__ == '__main__':
	app.run(host="127.0.0.1")
# to let others in...   app.run(host ="0.0.0.0")