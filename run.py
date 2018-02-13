# TO RUN THE SERVER
#  $ export FLASK_APP=run.py
# $ flask run

from flask import Flask, render_template
# import mysql.connector

app = Flask(__name__)

@app.route("/",methods=['GET'])
def main():
    return render_template('index.html')
@app.route("/test",methods=['GET'])
def getinfo():
    connection = mysql.connector.connect(host="localhost",user="root",password="", database="python")
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM infosPC""")
    rows = cursor.fetchall()
    return jsonify(data=cursor.fetchall())
if __name__ == "__main__":
    app.run()