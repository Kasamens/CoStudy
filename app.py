from flask import Flask, render_template

import os
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

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
