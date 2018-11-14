from flask import Flask, render_template, request, session, url_for, redirect
import os
import urllib
import json

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route("/", methods = ["POST", "GET"])
def input_field_page():
	searchQuery = "Batman"
	pageNumber = 1
	request = urllib.request.urlopen('http://www.omdbapi.com/?s=' + searchQuery + '&page=' + str(pageNumber) + '&apikey=42175782')
	data = json.loads(request.read())
	# print(data['Search'])
	return render_template('OMDbAPI.html', query=searchQuery, pageNum=pageNumber,movies=data['Search'])

if __name__ == "__main__":
	app.debug = True
	app.run()