# elephantSQL seperate db container deployment with django
deploy API to heroku in docker container
deploy Nextjs front to Vercel
deploy postgreSQL to elephantSQL

submit front end link on vercel

---------------------------------
> terminal command
- work in repo
**folder/file**

## setup
> $ mkdir elephant-demo

Use poetry to initialize folder 

> $ cd `elephant-demo` 
> $ poetry init -n 
> $ poetry shell 
> $ poetry add 

python = "^3.8"
django = "^3.0.8"
djangorestframework = "^3.11.0"
gunicorn = "^20.0.4"
whitenoise = "^5.1.0"
django-cors-headers = "^3.4.0"
django-environ = "^0.4.5"
psycopg2-binary = "^2.8.5"


> $ django-admin startproject snacks_api_project .

- sign up elephant sql

> $ python manage.py startapp snacks


# set up CRUD app

**project/settings.py**
- change DB from SQLite to postgreSQL

> $ python manage.py createsuperuser 

- check elephantSQL
super user has added info to db size

**snacks/models.py**
- make model > name & str

touch **snacks/serializers.py**
class Meta > fields & model

**snacks/views.py**
import models and serialixer
create views > queryset & serializer_class

touch **snacks/urls.py**
snack list

**project/urls.py**
snacks.urls 
   ^
  app

**snacks/urls.py**
import views
snack detail

**project/settings.py**
--installed apps--
app & restframework

> $ python manage.py makemigrations snacks
                                       ^
                                    app name
> $ python manage.py migrate

add something/snack in django local host view

look at db in elephantSQL with 
SELECT * FROM snacks_snacks;
                ^       ^
            app name _ model name

**snacks/views.py**
snack detail

**snacks/urls.py**
snack detail

# start deploy to heroku
run local then heroku

touch **Dockerfile**

touch **requirements.txt**
> $ poetry export -f requirements.txt -o requirements.txt

get docker compose

docker-compose up -d
    first time will build on its own

looks gross because assets are lost in container
use whitenoise to gather static so it looks normal

settings
install apps whitenoise after security, before session
intall apps cors middle ware first


middle ware 
cors
whitenoise

static files 
statics 
cors 


allowed hosts - dev does not add for you
local host 

settings environ


touch .env INSIDE PROJECT FOLDER

moved to env

docker compose down 

docker compose up --build - d

collect static files INSIDE CONTAINER
create empty static folder

debug on handles static for you 
debug off while in production ! 

now running locally in a container talking to database in iowa

# -- deploy to heroku --
have heroku CLI

exit venv

> $ heroku -v

> $ heroku create elephant-demo

touch heroku yml

git init


> $ heroku git:remote -a elephant-demo    
                          ^
                        heroku app name

current remotes : GitHub & Heroku
                    ^         ^
         origin master        heroku master

make git ignore before commit

> $ heroku stack:set container

> $ git push heroku master

add heroku to allowed hosts
heroku does not have env

add env to config vars on heroku app
