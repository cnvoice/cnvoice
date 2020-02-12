## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)


## Running Locally

Make sure you have Python 3.7 [installed locally](http://install.python-guide.org). To push to Heroku, you'll need to install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli), as well as [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```sh
$ git clone https://github.com/cnvoice/cnvoice.git
$ cd cnvoice

$ python3 -m venv cnvoice
$ pip install -r requirements.txt

$ heroku local
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)
