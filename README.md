### InstaShare (Django v5.1.1)

#### Steps
- First, install the dependencies:
```sh
pip install -r requirements.txt
```
- You will need a PostgreSQL database server
- Create a file `.env` in the root folder and set the following environment variables:
    - `DB_HOST`
    - `DB_DATABASE`
    - `DB_USER`
    - `DB_PASSWORD`
    - `DB_PORT`

  pointing to your PostgreSQL database
- Run the migrations to create the database structure: 
```sh
python manage.py migrate
```
 
- Install Redis
- Add another environment variable pointing to your Redis instance: `REDIS_URL`

- Run Celery:
```sh
 celery -A djangobackend worker --loglevel=INFO
 celery -A djangobackend beat --loglevel=INFO
 ```

- Run the server:
```sh
python manage.py runserver
```

#### Tests
-  For running tests: 
```sh
python manage.py test
```

#### Frontend repo
The frontend for this Django project is this: [Angular frontend](https://github.com/xero-q/angular-frontend).