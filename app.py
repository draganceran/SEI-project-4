from flask import Flask, jsonify
from pony.orm import Database
app = Flask(__name__)

app = Flask(__name__)
db = Database()

db.bind(provider='postgres', database='project4')

# from config import routes
db.generate_mapping(create_tables=True)
@app.errorhandler(404)
def not_found(_error):
    return jsonify({'message':'Not found'}), 404
