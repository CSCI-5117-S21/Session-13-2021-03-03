# in-class 2021-02-13
(WARNING WARNING WARNING) -- README COPPIED FROM A PREVIOUS PROJECT -- the autho0 setup isn't necissary.

### local setup:

```
# setup
pipenv install
pipenv shell
```

### heroku setup:

```
heroku create
heroku addons:create heroku-postgresql:hobby-dev
heroku config # take note of the DATABASE_URL
cp .env.example .env
# modify .env to have the DATABASE_URL
heroku pg:psql # run the commands in schema.sql
```
### Run remotely
```
git add .
git commit -m "setting up heroku"
git push heroku main
heroku open
```

### run locally
```
# setup
pipenv install
pipenv shell
heroku local dev
```

