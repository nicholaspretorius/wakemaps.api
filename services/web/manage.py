from flask.cli import FlaskGroup

from project import app, db
from project.models import Wakepark

cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    wakepark = Wakepark(name="Stoke City Wakepark")
    wakepark.insert()


if __name__ == "__main__":
    cli()
