from flask import Flask, render_template, request, redirect
from requests import get, post
from resources import api
from database import User, db

app = Flask(__name__)
api.init_app(app)
db.init_app(app)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sqlite3'

@app.route('/home', methods = ['GET','POST'])
def home_page():
  if request.method == 'POST':
    name = request.form.get('username')
    #make request to API
    response = get(f'http://127.0.0.1:5000/api/user/{name}')
    response = response.json()
    return render_template('show.html', response = response)
  return render_template('front.html')

@app.route('/create', methods = ['GET','POST'])
def info_page():
  if request.method == 'POST':
    username = request.form.get('username')
    email = request.form.get('email')
    course = request.form.get('course')
    institute = request.form.get('insti')
    about = request.form.get('about')
    response = post('http://127.0.0.1:5000/api/user', data = {'username': username, 'email': email, 'course': course, 'institute': institute, 'about': about})
    return redirect('/home')

  return render_template('create.html')

if __name__ == "__main__":
  app.run(debug = True)