from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db_uri = 'mysql+pymysql://root:@127.0.0.1/bbs_db'
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
db = SQLAlchemy(app)

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.Text())
    content = db.Column(db.Text())

@app.route("/")
def bbs():

    posts = Post.query.all()

    return render_template("bbs.html", posts = posts)