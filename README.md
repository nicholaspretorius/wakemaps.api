## Running the app

### Local Computer:

* `export FLASK_APP=project/__init__.py; python manage.py run`

### Docker Container:

* `docker-compose build` - to build the images
* `docker-compose up` - to start the containers
* `docker-compose down` - to stop the containers
* `docker-compose down -v` - to stop the containers and take down the volume

When running for the first time, (or anytime the volumes are taken down), run: 

* `docker-compose exec web python manage.py seed_db`

This will seed the db with some basic data. 

To connect to the database and check the contents: 

* `docker-compose exec db psql --username=postgres`
* `\l` - lists all the databases
* `\c wakemaps_test` - connect to the wakemaps_test database
* `\d` - to view the tables
* `\dt` - to view the schema
* `SELECT * FROM wakeparks;` - to see what is in the table

To verify the volume is created run: 

* `docker volume inspect wakemaps.api_postgres_data`
