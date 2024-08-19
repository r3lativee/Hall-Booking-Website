from flask import Flask, render_template, session, redirect, url_for
from functools import wraps
import pymongo

app = Flask(__name__)
app.debug = True
app.secret_key = "ADBU"

# Database
client = pymongo.MongoClient('localhost', 27017)
db = client.adbu
date = db.date


# client = pymongo.MongoClient('localhost', 27017)
# db = client.dates

# Decorators
def login_required(f):
  @wraps(f)
  def wrap(*args, **kwargs):
    if 'logged_in' in session:
      return f(*args, **kwargs)
    else:
      return redirect('/')
  
  return wrap

# Routes
from user import routes

@app.route('/')
def home():
  return render_template('index.html')
  if request.method == 'POST':
    return redirect(url_for('/log'))


@app.route('/log', methods=['GET', 'POST'])
def log():
    return render_template('home.html')


@app.route('/dashboard/',methods=['GET', 'POST'])
@login_required
def dashboard():
  data = db.date.find()
  for x in data:
    print(date)
  return render_template('dashboard.html')

  # if request.method == 'POST':
  #   return redirect(url_for('/dashboard/'))


