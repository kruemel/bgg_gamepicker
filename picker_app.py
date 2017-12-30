from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/process', methods=['POST'])
def process():

    username = request.form['username']

    if username:
        return jsonify({'username' : username})
    return jsonify({'error' : 'Missing data!'})

if __name__ == '__main__':
    app.run(debug=True)
