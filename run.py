# TO RUN THE SERVER
#  $ export FLASK_APP=run.py
# $ flask run

from flask import Flask, render_template
import os
import psycopg2

app = Flask(__name__)

@app.route("/",methods=['GET'])
def main():
    return render_template('index.html')
@app.route("/test",methods=['GET'])
def getinfo():
    
    return jsonify(data=cur.fetchall())

if __name__ == "__main__":
    app.run()