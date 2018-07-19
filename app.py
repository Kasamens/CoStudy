from flask import Flask, render_template
import urllib.parse as urlparse
import psycopg2
import os
import datetime
app = Flask(__name__)



def connect_to_database():
    conn = ""
    out = []
    url = urlparse.urlparse(os.environ['DATABASE_URL'])
    dbname = url.path[1:]
    user = url.username
    password = url.password
    host = url.hostname
    port = url.port
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
    return conn.cursor()

def insert_into_database(text,type):
    try:
        cur = connect_to_database()
        cur.execute("""INSERT INTO thought VALUES(text,datetime.now(),type,0,)""")    
    except:
        '%s text not inserted', text

def get_thoughts():
    try:
        cur = connect_to_database()
        cur.execute("""SELECT text from thought""")
        out = cur.fetchall()
    except:
        out = {"err": "General SQL Error"}
    return out


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route('/img/<path:path>')
def send_js(path):
    return send_from_directory('img', path)

@app.route('/css/<path:path>')
def send_js(path):
    return send_from_directory('css', path)

@app.route('/posts')
def posts():
    thoughts = get_thoughts()
    return render_template('posts.html', thoughts=thoughts)



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
