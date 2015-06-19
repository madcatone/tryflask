#-*- coding:utf-8 -*-
from flask import Flask, render_template, session, redirect, url_for, escape, request
from flask_bootstrap import Bootstrap
import db_conn.pgsql_conn_new as pgsql_conn
import db_conn.sqlalchemy_conn as alchemy_conn
import _uniout

app = Flask(__name__)
Bootstrap(app)
@app.route('/')
@app.route('/index')
#def index():
#    records = pgsql_conn.select()
    #return records
#    return render_template('index.html', records=records)
def index():
    if 'username' in session:
        #return 'Logged in as %s' % escape(session['username'])
        tuple_records = pgsql_conn.select()
        records = list(tuple_records)
        for i in records:
        	print _uniout.unescape(i[5], 'utf8')
        return render_template('index.html', records=records)
    return 'You are not logged in  </br><a href="login" class="btn btn-primary" role="button">Login</a> \
            <a href="bendon" class="btn btn-primary" role="button">Bendon</a>'

@app.route('/about')
def about():
    records = Table('problem_mail', alchemy_conn.metadata, autoload=True)
    r = records.select(users.id == 1).execute().first()
    return render_template('about.html', records=r)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/bendon', methods=['GET', 'POST'])
def bendon():
    # bendom
    if request.method == 'POST':
        session['username'] = request.form['username']
        return 'You are : %s' %session['username']
    return '''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
if __name__ == '__main__':
    app.run(debug=True)
