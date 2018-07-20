from flask import Flask, render_template, request,redirect,url_for
import models 
import os
from flask import flash


app = Flask(__name__)

app.config['SECRET_KEY'] = 'v5d&fiouf3pwht^^2ja5r!q7ex3e)294dj)xr%668e5845^)oz'

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/posts')
def posts():
    thoughts = models.DataModel.get_from_database("""SELECT text from thought""")
    return render_template('Posts.html', thoughts=thoughts)



@app.route('/login', methods=('GET', 'POST'))
def login():
    form = models.LoginForm()
    if request.method == 'POST':
        query = models.DataModel.get_from_database("""SELECT password FROM users WHERE email = %s""", request.form['email'])
    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template('Login.html', form=form)

@app.route('/sign-up', methods = ['GET', 'POST'])
def signup():
    form = models.SignUpForm()
    if request.method == 'POST':
        #models.DataModel.insert_into_database("""INSERT INTO users VALUES (%s, %s, %s, %s, %s);,"","","",request.form['email'],request.form['password'])                             
        flash('You signed up successfully')
        return redirect(url_for('index'))
    return render_template('SignUp.html', form=form)

@app.route('/about')
def about():
    return render_template('AboutUs.html')

@app.route('/profile')
def profile():
    return render_template('Profile.html')


@app.route('/add_thought', methods = ['GET', 'POST'])
def add_thought(type):
    form = models.ThoughtForm()
    if request.method == 'POST' and form.validated():
        models.DataModel.insert_into_database("""INSERT INTO thought VALUES(request.form['text'])""")
        flash('Uploaded successfully')
        return redirect(url_for(posts))
    return render_template('Posts.html', form=form)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)






@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('img', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)

@app.route('/fonts/<path:path>')
def send_fonts(path):
    return send_from_directory('fonts', path)

@app.route('/bootstrap/<path:path>')
def send_bootstrap(path):
    return send_from_directory('bootstrap', path)

