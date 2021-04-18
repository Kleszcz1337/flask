from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMNY_DATABASE_URL'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.string(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    data_created = db.Column(db.DataTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id



@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug = True)