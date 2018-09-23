#Sajed Nahian
#SoftDev1 pd6
#K08 -- Fill Yer Flask
#2018-09-20

from flask import Flask, render_template
import hw06

app = Flask(__name__) # create instance of class Flask


@app.route("/occupations") #assign fxn to route
def occupations_page():
    return render_template('occupations.html', headings = hw06.headings, randomlySelectedJob = hw06.pickRandomOccupation(), occupations = hw06.occupationsDictionary)

if __name__ == "__main__":
    app.debug = True
    app.run()