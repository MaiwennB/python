# TO RUN THE SERVER
# $ export FLASK_APP=run.py
# $ flask run
import mysql.connector
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/",methods=['GET'])
def main():
    return render_template('index.html')
@app.route("/get",methods=['GET'])
def getinfo():
    connection = mysql.connector.connect(host="localhost",user="root",password="root", database="python")
    cursor = connection.cursor()
    cursor.execute("""SELECT id, nomHost, disk, OS, CPU_STAT FROM infosPC""")
    info = cursor.fetchall()
    return jsonify(info)
if __name__ == "__main__":
    app.run()