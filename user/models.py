from flask import Flask, jsonify, request, session, redirect
from passlib.hash import pbkdf2_sha256
from app import db
import uuid
from app import date


# for user input
class User:

  def start_session(self, user):
    del user['password']
    session['logged_in'] = True
    session['user'] = user
    return jsonify(user), 200

  def signup(self):
    print(request.form)

    # Create the user object
    user = {
      "_id": uuid.uuid4().hex,
      "name": request.form.get('name'),
      "email": request.form.get('email'),
      "password": request.form.get('password')
    }

    # Encrypting the password
    user['password'] = pbkdf2_sha256.encrypt(user['password'])

    # Check for existing email address
    if db.users.find_one({ "email": user['email'] }):
      return jsonify({ "error": "Email address already in use" }), 400

    if db.users.insert_one(user):
      return self.start_session(user)

    return jsonify({ "error": "Signup failed" }), 400
  
  def signout(self):
    session.clear()
    return redirect('/')
  
  def login(self):

    user = db.users.find_one({
      "email": request.form.get('email')
    })

    if user and pbkdf2_sha256.verify(request.form.get('password'), user['password']):
      return self.start_session(user)
    
    return jsonify({ "error": "Invalid login credentials" }), 401





# for date entry of halls
# class Date:
  def book(self):
    # print(request.form)

    date = {
      
      # "__id": uuid.uuid4().hex,
      "name_booker":request.form.get('name_booker'),
      "reason":request.form.get('reason'),
      "dates":request.form.get('dates'),
      "start_time":request.form.get('start_time'),
      "end_time":request.form.get('end_time'),
    }


    #comparing with existing data
    if db.date.find_one({"dates" : date['dates']}):
      if db.date.find_one({"start_time" : date['start_time']}) and ({"end_time" : date['end_time']}):
        return jsonify({"error":"Already Booked"}), 400
    
    #if slot is empty book
    if db.date.insert_one(date):
      return jsonify({"error":"You have successfully Booked!!"}), 400
    

    # return jsonify({"date":"date inserted"}), 200


