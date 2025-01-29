#816037651 David Williams Lab1 Attempt
from flask import Flask, request, jsonify
import json

from markupsafe import escape

from collections import Counter
import math


app = Flask(__name__)

global data

# read data from file and store in global variable data
with open('data.json') as f:
    data = json.load(f)


@app.route('/')
def hello_world():
    return 'Hello, World!'  # return 'Hello World' in response

@app.route('/students')
def get_students():
    return jsonify(data) # return student data in response

@app.route('/students/<id>')
def get_student(id):
    result = []
    pref = request.args.get('pref') # get the parameter from url
    if pref:
        for student in data: 
          if student['pref'] == pref: # select only the students with a given meal preference
              result.append(student) # add match student to the result
          return jsonify(result) # return filtered set if parameter is supplied
        return jsonify(data) # return entire dataset if no parameter supplied

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'


@app.route('/stats')
def get_stats():
    pref = Counter([student['pref'] for student in data])
    programme = Counter([student['programme'] for student in data])
    #return jsonify({ 'preference': dict(pref), 'programmes': dict(programme)})
    return jsonify(pref + programme)

@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    ans = a + b
    return jsonify({'added' : ans})

@app.route('/subtract/<int:a>/<int:b>')
def subtract(a, b):
    ans = a - b
    return jsonify({'subtracted' : ans})

@app.route('/multiply/<int:a>/<int:b>')
def multiply(a, b):
    ans = a * b
    return jsonify({'multiplied' : ans})

@app.route('/divide/<int:a>/<int:b>')
def divide(a, b):
    ans = a / b
    return jsonify({'divided' : ans})












#@app.route('/stats')
#chicken = 0
#fish = 0
#veg = 0
#compsciM = 0
#compsciS = 0
#itM = 0
#itS = 0


#def get_student(id):


#        for student in data: 
 #           if student['pref'] == 'Chicken': 
#                chicken += 1
 #           if student['pref'] == 'Fish': 
  #              fish += 1
   #         if student['pref'] == 'Vegetable': 
    #            veg += 1
     #       if student['programme'] == 'Computer Science (Major)': 
      #          compsciM += 1
       #     if student['programme'] == ''Computer Science (Special)': 
        #        compsciS += 1
         #   if student['programme'] == 'Information Technology (Major)': 
          #      itM += 1
#            if student['programme'] == 'Information Technology (Special)': 
 #               itS += 1
              # select only the students with a given meal preference
  #            result.append(student) # add match student to the result
   #       return jsonify(result) # return filtered set if parameter is supplied
    #    return jsonify(data) # return entire dataset if no parameter supplied
    
  

app.run(host='0.0.0.0', port=8080, debug=True)
