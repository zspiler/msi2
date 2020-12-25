from flask import Flask, request, render_template
from pymongo import MongoClient
from redis import Redis 

app = Flask(__name__)
db = MongoClient("mongodb://db:27017").test_db
redis = Redis(host='redis', port=6379)


counter = db.col.find_one()
if counter == None:
    db.col.insert_one({ 'counter' : 1 })

if redis.get('hits') == None:
    redis.incr('hits')


@app.route('/', methods=['GET', 'POST'])
def main():
    counter = db.col.find_one()['counter'] 
    if request.method == 'POST':
        redis.incr('hits')
        counter += 1
        db.col.find_one_and_update({}, {'$set': { 'counter': counter }})
    return render_template('index.html', x=counter, hits=int(redis.get('hits'))) 

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')

# cat pictures?