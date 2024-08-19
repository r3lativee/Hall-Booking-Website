from flask import Flask
from app import app
from user.models import User
# from user.models import Date


@app.route('/user/signup', methods=['POST'])
def signup():
  return User().signup()

@app.route('/user/signout')
def signout():
  return User().signout()

@app.route('/user/login', methods=['POST'])
def login():
  return User().login()

@app.route('/date/book', methods=['POST'])
def book():
  return User().book()