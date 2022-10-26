Фамилия и имя:
    
    Аданов Болот

Для начало сделайте копию проекта

    git clone git@github.com:adanovbolot/test_city_and_street_and_shop.git

Создание виртуального окружения

    python -m venv env

Чтобы начать пользоваться виртуальным окружением, необходимо его активировать: venv\Scripts\activate. bat - для Windows; source venv/bin/activate - для Linux и MacOS.

docker-compose build собираем контейнер

    sudo docker-compose build

запуск docker compose для проверки

    sudo docker-compose up -d


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
    
    sudo docker-compose run web python manage.py makemigrations
    sudo docker-compose run web python manage.py migrate

После создания структуры базы данных вы можете создать учетную запись администратора:

    sudo docker-compose run web python manage.py createsuperuser

Открыв порт, вы можете проверить правильность работы вашей базы данных. Запустите сервер разработки Django:

    sudo docker-compose run web python manage.py runserver

url:

    GET/city/ — получение всех городов из базы;
    GET /city/city_id/ — получение города по id;
    GET /city/city_id/street/ — получение всех улиц города; (city_id — идентификатор города)
    POST /shop/ — создание магазина; Данный метод получает json c объектом магазина, в
    ответ возвращает id созданной записи.
    GET /shop/ - действия: filter


Параметр open: 0 - закрыт, 1 - открыт. Данный статус определяет исход из
параметров «Врем открытия», «Врем закрытия» и текущего времени сервера.

не понял


буду рад получить, советы как было бы лучше сделать
