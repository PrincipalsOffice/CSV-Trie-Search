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
