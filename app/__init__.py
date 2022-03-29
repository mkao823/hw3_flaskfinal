from flask import Flask

myobj = Flask(__name__)
myobj.config.from_mapping(SECRET_KEY='password')
from app import routes

