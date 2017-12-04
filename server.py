from flask import render_template, Flask, request, jsonify
from trie import Trie
import csv


app = Flask(__name__)
trie = Trie()
with open('top-1m.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        trie.insert(row[1])


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/autocomplete')
def autocomplete():
    query = request.args.get('query')
    return jsonify(trie.start_with(query))
