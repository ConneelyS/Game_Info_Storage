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
    }

]

@app.route('/')
def home();
    return render_template('home.html')

@app.route('/games')
def games();
    return render_template('games_list.html', posts = posts)

if __name__ == '__main__':
    app.run(debug = True)