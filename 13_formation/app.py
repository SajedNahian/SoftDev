#Sajed Nahian
#SoftDev1 pd6
#K13: Echo Echo Echo
#2018-09-27

from flask import Flask, render_template, request

app = Flask(__name__) # create instance of class Flask


@app.route("/") #assign fxn to route
def input_field_page():
    return render_template('InputFields.html')

@app.route("/auth", methods = ['GET', 'POST'])
def auth_page():	
	usernameInfo = request.args['username'] if request.method == "GET" else request.form['username']
	return render_template('Authorize.html', username = usernameInfo, method = request.method)

if __name__ == "__main__":
    app.debug = True
    app.run()
