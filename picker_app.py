from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import ARRAY
from boardgamegeek import BGGClient, exceptions

app = Flask(__name__)

# on linux:
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://kathrin@dlocalhost/gamepicker'

# on windows:
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://kathrin:password@localhost:5433/gamepicker'
db = SQLAlchemy(app)

# db Models
class Game(db.Model):
    gid = db.Column(db.Integer, primary_key=True)
    name_col = db.Column(db.String(100), nullable=False)
    name_en = db.Column(db.String(100), nullable=False)
    authors = db.Column(ARRAY(db.String(40)))
    maxplayers = db.Column(db.Integer)
    minplayers = db.Column(db.Integer)
    max_playing_time = db.Column(db.Integer)
    min_playing_time = db.Column(db.Integer)
    best_playnum = db.Column(ARRAY(db.Integer))
    not_recom_playnum = db.Column(ARRAY(db.Integer))
    description = db.Column(db.Text)
    imageurl = db.Column(db.String(200))
    mechanics = db.Column(ARRAY(db.String(20)))
    average_weight = db.Column(db.Float)
    best_playnum = db.Column(ARRAY(db.Integer))

class GameQuery(db.Model):
    qid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    playnum = db.Column(db.Integer)
    max_playtime = db.Column(db.Integer)
    weight = db.Column(db.Integer)


@app.route('/')
def index():
    return render_template('userform.html')

@app.route('/processuser', methods=['POST'])
def process():
    username = request.form['username']
    
    if username:
        bgg = BGGClient()
        try:
            collection = bgg.collection(username, exclude_subtype='boardgameexpansion', own=True, wishlist=None)
            numgames = len(collection)
            return jsonify({'username' : username, 'numgames': numgames})
        except:
            return jsonify({'error' : 'Oops! An error occured. Most likely I could not find this username..'})
    return jsonify({'error' : 'Missing data!'})


if __name__ == '__main__':
    app.run(debug=True)
