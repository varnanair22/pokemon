The first thing to do is to clone the repository:

$ git clone https://github.com/varnanair22/pokemon.git
$ cd pokemon_app

Create a virtual environment to install dependencies in and activate it:

$ virtualenv2 --no-site-packages env
$ source env/bin/activate

Then install the dependencies:

(env)$ pip install -r requirements.txt
Note the (env) in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by virtualenv2.

Once pip has finished downloading the dependencies:

(env)$ cd pokemon
(env)$ python manage.py runserver

And navigate to http://127.0.0.1:8000/ for listing the pokemons.

http://127.0.0.1:8000/admin used to add, edit and delete pokemons using admin module.
Credentials:
Username - admin
Password - admin123

http://127.0.0.1:8000/add_pokemon used for adding pokemons via api.
Enter the api, based on its response pokemon details will be added in database avoiding duplicacy.
