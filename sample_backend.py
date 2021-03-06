from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route('/')

def hello_world():
   return 'Hello, World!'

users = { 
   'users_list' :
   [
      { 
         'id' : 'xyz789',
         'name' : 'Charlie',
         'job': 'Janitor',
      },
      {
         'id' : 'abc123', 
         'name': 'Mac',
         'job': 'Bouncer',
      },
      {
         'id' : 'ppp222', 
         'name': 'Mac',
         'job': 'Professor',
      }, 
      {
         'id' : 'yat999', 
         'name': 'Dee',
         'job': 'Aspring actress',
      },
      {
         'id' : 'zap555', 
         'name': 'Dennis',
         'job': 'Bartender',
      }
   ]
}

@app.route('/users', methods=['GET', 'POST', 'DELETE'])
def get_users():
   if request.method == 'GET':
      search_username = request.args.get('name')
      search_job = request.args.get('job')
      if search_username:
         subdict = {'users_list' : []}
         for user in users['users_list']:
            if user['name'] == search_username:
               if search_job and user['job'] == search_job:
                  subdict['users_list'].append(user)
               if not search_job:
                  subdict['users_list'].append(user)
         return subdict
      return users
   
   elif request.method == 'POST':
      users['users_list'].append(request.get_json())
      resp = jsonify(success = True)
      return resp

   elif request.method == 'DELETE':
      search_id = request.args.get('id')
      if search_id:
         for user in users['users_list']:
            if user['id'] == search_id:
               users['users_list'].remove(user)
               return jsonify(success=True)

   return users

@app.route('/users/<id>')
def get_user(id):
   if id:
      for user in users['users_list']:
         if user['id'] == id:
            return user
      return ({})
   return users