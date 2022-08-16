from distutils.log import debug
from flask import Flask, render_template
app = Flask(__name__)

posts= [
    {
        "name": "Borderlands",
        "release_year": "2009",
        "age_rating": "18",
        "score": "90",
        "developer": "Gearbox Software",
        "description": "Borderlands is an open shooter game with lots of loot"
    },

    {
        "name": "Fortnite",
        "release_year": "2017",
        "age_rating": "12",
        "score": "70",
        "developer": "Epic Games",
        "description": "Building game with lots of players"
    },

    {
        "name": "Borderlands 2",
        "release_year": "2014",
        "age_rating": "18",
        "score": "95",
        "developer": "Gearbox Software",
        "description": "Borderlands 2 is an open shooter game with even more loot"
    },

    {
        "name": "Call of Duty 4: Modern Warfare",
        "release_year": "2007",
        "age_rating": "15",
        "score": "80",
        "developer": "Activision",
        "description": "Modern Warfare is a first-person shooter game"
    }


]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/games')
def games():
    return render_template('games_list.html', posts = posts)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug = True)