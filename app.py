from flask import Flask, request, render_template
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://db:27017")
db = client.test_db


counter = db.col.find_one()
if counter == None:
    db.col.insert_one({ 'counter' : 1 })


@app.route('/', methods=['GET', 'POST'])
def main():
    counter = db.col.find_one()['counter']
 
    if request.method == 'POST':
        counter += 1
        db.col.find_one_and_update({}, {'$set': { 'counter': counter }})
        
    return render_template('index.html', counter=counter) 

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')
