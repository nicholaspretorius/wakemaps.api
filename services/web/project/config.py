import os

basedir = os.path.abspath(os.path.dirname(__file__))

DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

db_path = "postgres://{}/{}".format(
    f'{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}', DB_NAME)


class Config(object):
    SQLALCHEMY_DATABASE_URI = db_path
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    STATIC_FOLDER = f"{os.getenv('APP_FOLDER')}/project/static"
