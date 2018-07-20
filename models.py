
import urllib.parse as urlparse
import psycopg2
import os
import json
import datetime
import routes

#form imports
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField
from wtforms.validators import DataRequired,Length, EqualTo
from passlib.hash import sha256_crypt

class DataModel:
    
    def connect_to_database(self):
        try:
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
        except Exception as e:
            out = {'err' : str(e)}
            return json.dumps(out)

    def insert_into_database(self,query):
        try:
            cur = connect_to_database()
            cur.execute(query)    
        except Exception as e:
            out = {"err": str(e)}
        return json.dumps(out)
            

    def get_from_database(self,query):
        try:
            cur = self.connect_to_database()
            cur.execute(query)
            out = cur.fetchall()
            return out
        except Exception as e:
            out = {"err": str(e)}
        return json.dumps(out)



class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(min=1, max=50)])
    password = PasswordField('password', validators=[DataRequired()])


class SignUpForm(FlaskForm):
    firstname = StringField('first name', validators=[DataRequired(), Length(min=1, max=50)])
    lastname = StringField('last name', validators=[DataRequired(), Length(min=1, max=50)])
    username = StringField('user name', validators=[DataRequired(), Length(min=1, max=50)])
    status = StringField('last name', validators=[DataRequired(), Length(min=1, max=50)])
    email = StringField('email', validators=[DataRequired(), Length(min=6, max=100)])
    password = PasswordField('password', validators=[DataRequired(), EqualTo('confirm', message='passwords should match')])
    confirm = PasswordField('confirm password')


class ThoughtForm(FlaskForm):
    text = TextAreaField('Your text goes here', validators=[DataRequired(), Length(min=1, max=1000)])