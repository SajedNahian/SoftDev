from flask import Flask, render_template, request, session, url_for, redirect
import os
import urllib
import json

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route("/", methods = ["POST", "GET"])
def input_field_page():
	videoUrl = ''
	with urllib.request.urlopen('https://api.nasa.gov/planetary/apod?api_key=E5cEaWdPE4Edf7N0luy673hxUFYvIJCAAPcGmPQN') as url:
		 data = json.loads(url.read().decode())
		 videoUrl = data['url']
	return render_template('NASAPage.html', youTubeVideoSource = videoUrl)

if __name__ == "__main__":
	app.debug = True
	app.run()