import time

from flask import Flask


app = Flask(__name__)
# db_cache = redis.Redis(host='redis', port=6379)


# def web_hit_cnt():
#     return db_cache.incr('hits')


# @app.route('/')
# def index():

#     cnt = web_hit_cnt()
#     return '''
#     <h1 style=color:deepskyblue;>docker-compose application</h1>
#     <p style=color:deepskyblue;>web access count: {} times</p>
#     '''.format(cnt)


if __name__ == "__main__":
    app.run()