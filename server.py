from flask import Flask, render_template
# import the class from friend.py
from occupations import occupations
app = Flask(__name__)
@app.route("/")
def index():
    # call the get all classmethod to get all friends
    occupationslist= occupations.get_all()
    print(occupations)
    return render_template("index.html", occupationslist = occupationslist)
            
if __name__ == "__main__":
    app.run(debug=True)

