from flask import render_template, Flask, request, jsonify
from trie import Trie
import csv


app = Flask(__name__)
trie = Trie()
count = 0
with open('top-1m.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        trie.insert(row[1])
        count += 1
        if count > 5000:
            break


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/autocomplete')
def autocomplete():
    query = request.args.get('query')
    # TODO: limit number of records start_with() returns
    return jsonify(trie.start_with(query))
