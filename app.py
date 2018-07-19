from flask import Flask, render_template
import urllib.parse as urlparse
import psycopg2
import os
app = Flask(__name__)


@app.route('/')
def index():
    conn = ""
    out = []
    try:
        url = urlparse.urlparse(os.environ['DATABASE_URL'])
        dbname = url.path[1:]
        user = url.username
        password = url.password
        host = url.hostname
        port = url.port
        conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
    except:
        out = {"err": "Unable to connect to the database"}

        cur = conn.cursor()
        cur.execute("""SELECT text from thought""")
        out = cur.fetchall()
    
    return render_template('index.html', out = thoughts)


@app.route('/new', methods = ['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['city'] or not request.form['addr']:
            flash('Please enter all the fields', 'error')
        else:
            user = User(request.form['name'], request.form['city'],
            request.form['addr'], request.form['pin'])

            db.session.add(user)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('show_all'))
		
    return render_template('new.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
