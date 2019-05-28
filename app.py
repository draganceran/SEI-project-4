from flask import Flask, jsonify
from pony.orm import Database

# tells us which folder/file we are in
app = Flask(__name__)
db = Database()
# Connects to the database
db.bind(provider='postgres', database='project4')
# pylint: disable=W0611,C0413
from config import routes # loads in the models and controllers

# creates the database tables based on the models
# must happen after tables are loaded
db.generate_mapping(create_tables=True)
@app.errorhandler(404)
def not_found(_error):
    return jsonify({'message':'Not found'}), 404
