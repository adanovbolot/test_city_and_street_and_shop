Создание базы данных и пользователя 

Войдите в интерактивную строку Postgres, набрав:

    sudo -u postgres psql

создадим базу данных для проекта

    CREATE DATABASE myproject;

создадим пользователя базы данных

    CREATE USER myprojectuser WITH PASSWORD 'password';

После этого нужно изменить несколько параметров подключения только что созданного пользователя. Это ускорит операции с базой данных (необходимые значения не придется запрашивать и устанавливать при каждом соединении).

    ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
    ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
    ALTER ROLE myprojectuser SET timezone TO 'UTC';

Осталось только предоставить пользователю БД права доступа к базе данных, которую вы создали:
    
    GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;

Выйдите из командной строки SQL
    
    \q



Поддержка БД Django

 вам нужно настроить его для поддержки созданной вами базы данных.
 
Откройте главный конфигурационный файл

settings.py

раздел DATABASES

        DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'myproject',
            'USER': 'myprojectuser',
            'PASSWORD': 'password',
            'HOST': 'localhost',
            'PORT': '',
        }
    }


Начать можно с создания миграций. Поскольку у вас еще нет фактических данных, эти команды просто создают исходную структуру базы данных:
    
    python manage.py makemigrations
    python manage.py migrate

После создания структуры базы данных вы можете создать учетную запись администратора:

    python manage.py createsuperuser

Открыв порт, вы можете проверить правильность работы вашей базы данных. Запустите сервер разработки Django:

    python manage.py runserver 0.0.0.0:8000

