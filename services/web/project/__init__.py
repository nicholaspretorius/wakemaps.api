from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)


class Wakepark(db.Model):
    __tablename__ = 'wakeparks'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)

    def __init__(self, name):
        self.name = name

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name
        }


@app.route('/')
def hello():
    return jsonify({'hello': 'world!'})


@app.route('/wakeparks', methods=['GET'])
def retrieve_wakeparks():
    try:
        wakeparks = Wakepark.query.order_by('id').all()
        formatted = [wakepark.format() for wakepark in wakeparks]

        return jsonify({
            'wakeparks': formatted,
            'total': len(formatted)
        })
    except():
        abort(500)
