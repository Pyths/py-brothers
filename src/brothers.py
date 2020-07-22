#OUTPUT
#{
#    "brothers": ["dannel", "joel", "eitan"]
#}
from flask import Flask
from flask import jsonify
import mysql.connector

brothers = []

cnx = mysql.connector.connect(user='root', password='admin',
                              host='localhost',
                              database='db_brothers',
                              port='3306')
cursor = cnx.cursor()
query = ("SELECT fname FROM tbl_brother")
cursor.execute(query)

for (fname) in cursor:
  print("{}".format(fname[0]))
  brothers.append(fname[0])

cursor.close()
cnx.close()
print("connecition esitoxa")

brothers_dict = {'brothers': brothers}
print("Brothers: " + ", ".join(brothers))

app = Flask(__name__)

@app.route('/')
def index_site():
    return "<h1>Welcome to brothers site, fuck you</h1>"

@app.route('/brothers')
def brothers_api():
    return jsonify(brothers_dict)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8070')



