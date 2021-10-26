# rmwebapp
Rmwebapp

```
@author: Brian
2021/10/25

```

Full Stack Developer.

Using the Django framework.

Download or git clone
https://github.com/bm33m/rmwebapp.git

The RM WebApp uses the MongoDB to save Data.
Hence the app needs Django and djongo.

Install the required dependencies.

1. Install and setup python.
2. Install and setup mongodb.
3. Install django.
4. Install djongo.

e.g.
```
pip install djongo

```

1. Start the server.
e.g.
```
cd pathto\MongoDB\Server\4.0\bin
pathto\MongoDB\Server\4.0\bin>mongod

 I NETWORK  [initandlisten] waiting for connections on port 27017

```
2. Create the database.
e.g.
```
cd pathto\MongoDB\Server\4.0\bin
pathto\MongoDB\Server\4.0\bin>mongo

> db
test
> show dbs
admin          0.000GB
config         0.000GB
local          0.000GB

> use rmwebappdb
switched to db rmwebappdb

```

3. Start the App.

e.g.
```
cd pathto\rmwebapp

$ py manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
October 25, 2021 - 08:39:31
Django version 3.0.5, using settings 'rmwebapp.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

```

Visit: http://127.0.0.1:8000/

Enjoy.
