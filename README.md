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
I chose the Python3+Flask stack since it's what I am most familiar with for prototyping. Instead of loading the datasets into a database, I implemented a simple in-menory trie.

Backend:
The server would load the csv into a trie in memory during startup, so it might take a while (~2 mins).

trie.py: A simplified version of Trie that only supports `insert()` and `start_with()`.
*  Each TrieNode stores a dictionary of its children Nodes.
*  Since the dataset is static and relatively small, I decided to store the current word in each TrieNode as well for simplier lookup logic.
*  I set a limit of 10 to the max number of words return by the Trie's `start_with()` method to improve the overall user experience.
*  In `start_with()`, I used BFS to traverse the trie so we can return results that are closest to the input length.
        
server.py: A flask web server with 2 simple endpoints:
*  `http://127.0.0.1:5000/`: servers the html/js/css
*  `http://127.0.0.1:5000/autocomplete`: takes a `query` param and return up to 10 suggestion results.

Frontend:
*  `templates/index.html`: A very barebone html/js page with an input and a submit button. Initially I tried to utilize the `<datalist>` html tag for displaying the automcomplete options, but since `<option>` does not support binding to onclick events, I could not achieve the "click and redirect" feature requirement with just `<datalist>`. So (again) due to time constraints I used a JS autocomplete library(https://github.com/Pixabay/JavaScript-autoComplete) instead.

TODO:
* Input validation 
* Unit tests
* Full text search? (suffix tree?)
