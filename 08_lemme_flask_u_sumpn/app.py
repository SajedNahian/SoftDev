#Sajed Nahian
#SoftDev1 pd6
#K08 -- Fill Yer Flask
#2018-09-20

from flask import Flask
app = Flask(__name__) # create instance of class Flask

header = '''
		<a href="/">Home</a>
		<a href="/about">About</a>
		<a href="/contact">Contact</a>
'''

@app.route("/") #assign fxn to route
def home_page():
    print (__name__)
    return header + "<h1>Home Page</h1>"

@app.route("/about") #assign fxn to route
def about_page():
    print (__name__)
    return header + "<h1>About Page</h1>"


@app.route("/contact") #assign fxn to route
def contact_page():
    print (__name__)
    return header + "<h1>Contact Page</h1>"

app.debug = True
app.run()
