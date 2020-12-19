import sys
from flask import Flask, request, render_template
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://db:27017")
db = client.test_db


counter = db.find_one()
if counter == None:
    db.insert_one({ 'counter' : 1 })

@app.route('/', methods=['GET', 'POST'])
def main():

    c = db.find_one()


    if request.method == 'POST':
        pass
    return render_template('index.html', counter=42) 

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')
