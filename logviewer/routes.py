
from flask import Flask, render_template
import os
import json 
 
app = Flask(__name__)
 
@app.route('/')
def home():
  files = os.listdir('./static/posts')  
  return render_template('home.html', logs = files )

@app.route('/about')
def about():
  return render_template('about.html')
 
@app.route('/log/<json>/')
def log(json):
   with open('./static/posts/'+ json) as file:
      file_lines = file.readlines() 
  
   return render_template('log.html', cont = file_lines)


if __name__ == '__main__':
    app.debug = True
    app.run(port=8000)



