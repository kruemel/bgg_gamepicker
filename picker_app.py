from flask import Flask, render_template, request, jsonify
from boardgamegeek import BGGClient, exceptions

app = Flask(__name__)

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
