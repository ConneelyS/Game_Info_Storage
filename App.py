from distutils.log import debug
from flask import Flask, render_template, request
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

@app.route('/register', methods = ['POST', 'GET'])
def register():
    if request.method == 'POST':
        try:
            new_username = request.form['new_username']
            new_password = request.form['new_password']

            with sql.connect("database.db") as connection:
                cur = connection.cursor()
                cur.execute("INSERT INTO user (username, password) VALUES (?,?)", (new_username, new_password))

                connection.commit()
                message = "New User Added Succesfully"
                
        except:
            connection.rollback()
            message = "Inserion Failed, Rollback Complete"

        finally:
            return render_template('new_user_added.html', message = message)
            connection.close()


if __name__ == '__main__':
    app.run(debug = True)