
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
# file dependencies
from main import app
from save.sql import SomeClass
# func
from func.func import getExample
# constants 
from constants.requests_constants import RequestsConstants
from constants.url_constants import UrlConstants


# auth
@app.patch(UrlConstants.reset)
def resetpassword():
    return getExample()

@app.post(UrlConstants.signIn)
def signIn():
    return getExample();

@app.post(UrlConstants.signUp)
def singUp():
    return getExample();

# user
@app.route( UrlConstants.user, methods = [RequestsConstants.get, RequestsConstants.post, RequestsConstants.delete])
def user():
    if request.method == RequestsConstants.get:
        return getExample();
    if request.method == RequestsConstants.post:
        return getExample();
    if request.method == RequestsConstants.delete:
        return getExample();

# contacts
@app.route( UrlConstants.actions, methods = [RequestsConstants.get, RequestsConstants.post, RequestsConstants.delete])
def actions():
    if request.method == RequestsConstants.get:
        return getExample();
    if request.method == RequestsConstants.post:
        return getExample();
    if request.method == RequestsConstants.delete:
        return getExample();

# actions
@app.route( UrlConstants.contacts, methods = [RequestsConstants.get, RequestsConstants.post, RequestsConstants.delete])
def contacts():
    if request.method == RequestsConstants.get:
        return getExample();
    if request.method == RequestsConstants.post:
        return getExample();
    if request.method == RequestsConstants.delete:
        return getExample();

# explore
@app.route( UrlConstants.explore, methods = [RequestsConstants.get, RequestsConstants.post, RequestsConstants.delete])
def explore():
    if request.method == RequestsConstants.get:
        return getExample();
    if request.method == RequestsConstants.post:
        return getExample();
    if request.method == RequestsConstants.delete:
        return getExample();

# stat 
@app.get(UrlConstants.stat)
def stat():
    return getExample();


# @app.post('/post')
# def post():
#     SomeClass.post(
#         request.json["title"]
#     )
#     return jsonify(SomeClass.get());


# @app.delete('/delete/<int:id>')
# def delete(id):
#     SomeClass.delete(id=id)
#     return jsonify( SomeClass.get());

if __name__ == "__main__":
    app.run(debug=True,port=5001)
