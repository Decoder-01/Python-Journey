from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('LogIn.html')
@app.route('/home')
def home__page():
    return render_template('Home.html')

@app.route('/home/about')
def about_page():
    return render_template('about.html')



