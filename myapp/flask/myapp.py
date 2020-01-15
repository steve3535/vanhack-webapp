from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)

app.config['MYSQL_HOST'] = '172.17.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'APPDB'

# Intialize MySQL
mysql = MySQL(app)


@app.route("/",methods=['GET','POST'])
def home():
    msg = ''
    if request.method == 'POST' and 'name' in request.form and 'pref_color' in request.form and 'animal' in request.form:
        #create variables
        name = request.form['name']
        pref_color = request.form['pref_color']
        animal = request.form['animal']
        #print name
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM foo WHERE name LIKE %s', [name])
        account = cursor.fetchone()
        # If account exists show error and validation checks
        if account:
            msg = 'Name already exists!'
        else:
            #Account doesnt exists and the form data is valid, now insert new account into accounts table
            cursor.execute('INSERT INTO foo VALUES (%s, %s, %s)', (name, pref_color, animal))

            mysql.connection.commit()
            msg = 'You have successfully inserted a record!'



    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'

    return render_template('home.html', msg=msg)


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=80)

