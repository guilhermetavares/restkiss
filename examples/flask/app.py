from flask import Flask
import redis
from restkiss.fl import FlaskResource
import time
app = Flask(__name__)


class UserResource(FlaskResource):
    def __init__(self, *args, **kwargs):
        super(UserResource, self).__init__(*args, **kwargs)
        self.conn = redis.StrictRedis(host='localhost', port=6379, db=0)

    def is_authenticated(self):
        return True

    def make_user_key(self, username):
        return 'user_{0}'.format(username)

    def list(self):
        usernames = self.conn.lrange('users', 0, 100)
        users = []

        for user in usernames:
            users.append(self.conn.hgetall(self.make_user_key(user)))

        return users

    def detail(self, username):
        return self.conn.hgetall(self.make_user_key(username))

    def create(self):
        key = self.make_user_key(self.data['username'])
        self.conn.hmset(
            key,
            {
                'username': self.data['username'],
                'email': self.data['email'],
                'added_on': int(time.time()),
            }
        )
        self.conn.rpush('users', self.data['username'])
        return self.conn.hgetall(key)


UserResource.add_url_rules(app, rule_prefix='/api/users/')

# Alternatively, if you don't like the defaults...
# app.add_url_rule('/api/users/', endpoint='api_users_list', view_func=UserResource.as_list(), methods=['GET', 'POST', 'PUT', 'DELETE'])
# app.add_url_rule('/api/users/<username>/', endpoint='api_users_detail', view_func=UserResource.as_detail(), methods=['GET', 'POST', 'PUT', 'DELETE'])

if __name__ == '__main__':
    app.debug = True
    app.run()
