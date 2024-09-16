### Django Backend Files upload system

#### Steps
- Run `pip install -r requirements.txt`
- Create a file `.env` in the root folder and set the following environment variables:
    - `DB_HOST`
    - `DB_DATABASE`
    - `DB_USER`
    - `DB_PASSWORD`
    - `DB_PORT`

  Pointing to your PostgreSQL database

- Run Celery
    - `celery -A djangobackend worker --loglevel=INFO`
    - `celery -A djangobackend beat --loglevel=INFO`
- Run `python manage.py runserver`