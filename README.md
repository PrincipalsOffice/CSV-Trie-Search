# CSV-Trie-Search

## Setting up a development environment (tested on Python3)

I assume that you have `git` and `python` installed.

    # Clone the code repository into current directory
    git clone git@github.com:PrincipalsOffice/CSV-Trie-Search.git my_app

    # Install flask
    pip install -r requirements.txt
    
    # Run the backend server
    export FLASK_APP=server.py
    flask run

Visit http://127.0.0.1:5000/ to test out the functionalities.


## Design considerations
I chose the Python3+Flask stack since it's what I am most familiar with for prototyping.

Due to time constraints, I was focused on delivering the required features, and there are certainly many parts that can be improved.


Backend:
    trie.py: A simplified version of Trie that only supports `insert()` and `start_with()`.
        - Each TrieNode stores a dictionary of its children Nodes.
        - Since the dataset is static and relatively small, I devided to store the current word in each TrieNode as well for simplier lookup logic.
        - I set a limit of 10 to the max number of words return by the Trie's `start_with()` method to improve the overall user experience.
        - In `start_with()`, I used BFS to traverse the trie so we can return results that are closest to the input length.
        
    server.py: A flask web server with 2 simple endpoints:
        `http://127.0.0.1:5000/`: servers the html/js/css
        `http://127.0.0.1:5000/autocomplete`: takes a `query` param and return up to 10 suggestion results.
