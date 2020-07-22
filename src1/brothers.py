#OUTPUT
#{
#    "brothers": ["dannel", "joel", "eitan"]
#}
from flask import Flask
from flask import jsonify
import mysql.connector

brothers = ["dannel", "joel", "eitan"]

brothers_dict = {'brothers': brothers}
print("Brothers: " + ", ".join(brothers))

app = Flask(__name__)

@app.route('/')
def index_site():
    return "<h1>Welcome to brothers site</h1>"

@app.route('/brothers')
def brothers_api():
    return jsonify(brothers_dict)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8070')



