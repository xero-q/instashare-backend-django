### Django Backend Files upload system

#### Steps
- Run `pip install -r requirements.txt`
- You will need a PostgreSQL database server
- Create a file `.env` in the root folder and set the following environment variables:
    - `DB_HOST`
    - `DB_DATABASE`
    - `DB_USER`
    - `DB_PASSWORD`
    - `DB_PORT`

  pointing to your PostgreSQL database
- Run `python manage.py migrate` to create the database structure
- Install Redis
- Add another environment variable pointing to your Redis instance: `REDIS_URL`
- Run Celery
    - `celery -A djangobackend worker --loglevel=INFO`
    - `celery -A djangobackend beat --loglevel=INFO`
- Run `python manage.py runserver`

#### Tests
-  For running tests: `python manage.py test`