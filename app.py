from flask import Flask, request, render_template
app = Flask(__name__)

x = 42

@app.route('/', methods=['GET', 'POST'])
def main():
    global x
    if request.method == 'POST':
        x += 1
    return render_template('index.html', counter=x) 

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')



# import time

# import redis
# from flask import Flask

# app = Flask(__name__)
# cache = redis.Redis(host='redis', port=6379)

# def get_hit_count():
#     retries = 5
#     while True:
#         try:
#             return cache.incr('hits')
#         except redis.exceptions.ConnectionError as exc:
#             if retries == 0:
#                 raise exc
#             retries -= 1
#             time.sleep(0.5)

# @app.route('/')
# def hello():
#     count = get_hit_count()
#     return 'Hello World! I have been seen {} times.\n'.format(count)