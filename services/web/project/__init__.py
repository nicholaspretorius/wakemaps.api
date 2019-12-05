from flask import Flask, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)

from . import models  # noqa


@app.route('/')
def hello():
    return jsonify({'hello': 'world!'})


@app.route('/wakeparks', methods=['GET'])
def retrieve_wakeparks():
    try:
        wakeparks = models.Wakepark.query.order_by('id').all()
        formatted = [wakepark.format() for wakepark in wakeparks]

        return jsonify({
            'wakeparks': formatted,
            'total': len(formatted)
        })
    except():
        abort(500)


@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory(app.config["STATIC_FOLDER"], filename)
