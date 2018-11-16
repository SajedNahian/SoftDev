from flask import Flask, render_template, request, session, url_for, redirect
import os
import urllib
import json

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route("/", methods = ["POST", "GET"])
def input_field_page():
	dogPicURL = ''
	while (dogPicURL[-3:].lower() != 'png'):
		request = urllib.request.urlopen('https://random.dog/woof.json')
		data = json.loads(request.read())
		dogPicURL = data["url"]

	request = urllib.request.urlopen('https://aws.random.cat/meow')
	data = json.loads(request.read())
	catPicURL = data["file"]
	print("--------------------------")
	print(catPicURL)
	print("--------------------------")

	
	request = urllib.request.urlopen('https://catfact.ninja/facts')
	data = json.loads(request.read())
	# print("--------------------------")
	# print(data["data"][0]["fact"])
	# print("--------------------------")
	catFact = data["data"][0]["fact"]
	return render_template('API-template.html', dogPicURL = dogPicURL, catPicURL =  catPicURL, catFact = catFact.lower()[0:-1])

if __name__ == "__main__":
	app.debug = True
	app.run()