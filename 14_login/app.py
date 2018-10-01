#ShowMeTheCode - Sajed Nahian Brian Lee
#SoftDev1 pd6
#K14: Do I Know You? 
#2018-10-01

from flask import Flask, render_template, request, session, url_for, redirect
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)

test_username = "test"
test_password = "test"

message = ""

@app.route("/", methods = ["POST", "GET"])
def input_field_page():
	global message
	if "username" in session:
		return render_template('Authorize.html', username = session["username"])
	print("Message: " + message)
	messageTemp = message
	message = ""
	return render_template('InputFields.html', login_message = messageTemp)

def check_user (username, password):
	return username == test_username and password == test_password

@app.route("/auth", methods = ["POST"])
def auth_page():
	global message
	if check_user(request.form['username'], request.form['password']):
		session["username"] = request.form["username"]
	else:
		if request.form['username'] != test_username:
			message = "Invalid username"
		else:
			message = "Invalid password"
	return redirect(url_for("input_field_page"))

@app.route("/logout")
def logout():
	global message
	session.pop("username")
	message = "Logged out successfully"
	return redirect(url_for("input_field_page"))

if __name__ == "__main__":
	app.debug = True
	app.run()