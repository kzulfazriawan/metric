import os
from flask import Flask

APP = Flask(__name__)
APP.config['JWT_SECRET_KEY'] = 'JWT-SECRET-KEY'
APP.config['SECRET_KEY'] = 'SECRET_KEY'
