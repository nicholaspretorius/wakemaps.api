import os

basedir = os.path.abspath(os.path.dirname(__file__))

DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')
DB_TEST_URL = os.getenv('DB_TEST_URL')

db_path = "postgresql://{}/{}".format(
    f'{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}', DB_NAME)

db_test_path = f'postgresql://{DB_TEST_URL}'


class BaseConfig(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    STATIC_FOLDER = f"{os.getenv('APP_FOLDER')}/project/static"


class DevelopmentConfig(BaseConfig):
    TESTING = False
    SQLALCHEMY_DATABASE_URI = db_path


class ProductionConfig(BaseConfig):
    TESTING = False
    SQLALCHEMY_DATABASE_URI = db_path


class TestConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = db_test_path
