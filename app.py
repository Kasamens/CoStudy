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
    cur = connect_to_database()
    cur.execute("""INSERT INTO thought VALUES(text,datetime.now(),type,0,)""")    


@app.route('/')
def index():
    return render_template('index.html')


def get_thoughts():
    try:
        cur = connect_to_database()
        cur.execute("""SELECT text from thought""")
        out = cur.fetchall()
    except:
        out = {"err": "General SQL Error"}
    return out


@app.route('/add_thought', methods = ['GET', 'POST'])
def add_thought():
    if request.method == 'POST':
        if not request.form['text']:
            flash('Please enter all the fields', 'error')
        else:
            insert_into_database(request.form['text'],'thought')
            flash('Record was successfully added')
            return redirect(url_for('index.html'))
		
    return render_template('add_thought.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
