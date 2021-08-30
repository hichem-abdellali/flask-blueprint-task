# Flask Blueprint Task

![Python](https://img.shields.io/badge/Python-v3.9.6-blue.svg?logo=python&longCache=true&logoColor=white&colorB=5e81ac&style=flat-square&colorA=4c566a)
![Flask](https://img.shields.io/badge/Flask-v1.1.2-blue.svg?longCache=true&logo=flask&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![Flask-Assets](https://img.shields.io/badge/Flask--Assets-v2.0-blue.svg?longCache=true&logo=flask&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![GitHub Last Commit](https://img.shields.io/github/last-commit/google/skia.svg?style=flat-square&colorA=4c566a&colorB=a3be8c&logo=GitHub)
# Getting Started

Flask Blueprint code to find the distance from the Moscow Ring Road to a specified address

setting the code is done in two steps:

### Environment Variables

Replace the values in **.env** :

* `FLASK_APP`: Entry point of your application; should be `wsgi.py`.
* `FLASK_ENV`: The environment in which to run your application; either `development` or `production`.
* `SECRET_KEY`: Randomly generated string of characters used to encrypt your app's data.
* `LESS_BIN` *(optional for static assets)*: Path to your local LESS installation via `which lessc` in linux or in windows install LESS with npm and set it to npm\\lessc.cmd.
* `ASSETS_DEBUG` *(optional)*: Debug asset creation and bundling in `development`.
* `LESS_RUN_IN_DEBUG` *(optional)*: Debug LESS while in `development`.
* `COMPRESSOR_DEBUG` *(optional)*: Debug asset compression while in `development`.


*Remember never to commit secrets saved in .env files to Github.*

### Installation

to deploy the server run these commands(dependencies version might differ from operating system):

```shell
$ git clone https://github.com/hackersandslackers/flask-blueprint-tutorial.git
$ cd flask-blueprint-tutorial
$ python3 -m venv .venv
$ venv\Scripts\activate
$ python3 -m pip install --upgrade pip
$ pip install -r requirements.txt
$ python3 wsgi.py

``` 

-----

Note that the path for the virtual environment(venv\Script\activate) depends on the operating system

The code was experimented on Windows10 with Python 3.9.6 using Pycharm 2020.2

**Thanks to Hackers and Slackers for their tutorials ![Flask Blueprint Tutorial]**
the core of the solution is inspired from their github https://github.com/hackersandslackers/flask-blueprint-tutorial/
