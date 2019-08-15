# simple-bike-ecommerce

**Initializing this project:**

1. Clone/Download this repo.
2. Create new virtual environment and activate it.
3. Install required packages `pip install -r requirenments.txt`
4. create `local_settings.py` along side `settings.py` inside `travel` with following configuration:

   ```
    DEBUG_STATE = True
    DB_ENGINE = 'django.db.backends.postgresql'
    DB_NAME = '<your db name>'
    DB_USER = '<your db user>'
    DB_PASSWORD = '<your db password>'
    DB_HOST = '127.0.0.1'
    CUSTOM_PORT = True
    DB_PORT = '5432'
    HOSTS = ['localhost']
   ```

   Make sure you have installed PostgreSQL. Check out official installation document as per your OS.

5. Run `python manage.py makemigrations` .
6. Run `python manage.py migrate` .
7. Finally start development server using `python manage.py runserver` .
