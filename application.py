from flask import Flask
application = Flask(__name__)


@application.route("/")
def home():
    return "Hello World!"


@application.route("/hello")
def hello():
    return "Hello World!"