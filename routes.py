from flask import Flask, render_template, request
import .app
app = Flask(__name__)



@app.route('/')
def index():
    test = app.get_thoughts()
    return render_template('index.html')



@app.route('/posts')
def posts():
    thoughts = get_thoughts()
    return render_template('Posts.html', thoughts=thoughts)

@app.route('/sign-up')
def sign_up():
    return render_template('SignUp.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        if not request.form['username'] or not request.form['password']:
            flash('All fields required', 'error')
        else:
            cur = connect_to_database()
            cur.execute("""SELECT password FROM users WHERE username = request.form['username']""")
            if form['password'] == cur:
                return redirect(url_for('index.html'))
            else :
                flash('Wrong password or username')
    return render_template('Login.html')

    return render_template('Login.html')

@app.route('/about')
def about():
    return render_template('AboutUs.html')

@app.route('/profile')
def profile():
    return render_template('Profile.html')


@app.route('/add_thought', methods = ['GET', 'POST'])
def add_thought(type):
    if request.method == 'POST':
        if not request.form['text']:
            flash('Please enter all the fields', 'error')
        else:
            insert_into_database(request.form['text'],type)
            flash('%s successfully uploaded', type)
            return redirect(url_for('post.html'))
    return render_template('add_thought.html')

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

