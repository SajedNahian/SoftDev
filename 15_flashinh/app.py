#ShowMeTheCode - Sajed Nahian Brian Lee
#SoftDev1 pd6
#K15: Oh yes, perhaps I do…  
#2018-10-02

from flask import Flask, render_template, request, session, url_for, redirect, flash
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)

test_username = "test"
test_password = "test"

@app.route("/", methods = ["POST", "GET"])
def input_field_page():
	if "username" in session:
		return render_template('Authorize.html', username = session["username"])
	return render_template('InputFields.html')

def check_user (username, password):
	return username == test_username and password == test_password

@app.route("/auth", methods = ["POST"])
def auth_page():
	if check_user(request.form['username'], request.form['password']):
		session["username"] = request.form["username"]
	else:
		if request.form['username'] != test_username:
			flash("Invalid username")
		if request.form['password'] != test_password:
			flash("Invalid password")
	return redirect(url_for("input_field_page"))

@app.route("/logout")
def logout():
	session.pop("username")
	flash("Logged out successfully")
	return redirect(url_for("input_field_page"))

if __name__ == "__main__":
	app.debug = True
	app.run()
