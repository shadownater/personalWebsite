# personalWebsite
A website that gives a general description of myself, shows off my art, as well as programming projects.

### Running on Windows pre-Creator's update

At root of project, run `workon myenv`, enabling virtual environment (virutalenv).
If you're not me for some reason, you'll need to run `pip install -r requirements.txt`.

Locally boot up the site using `python manage.py runserver`.

Deploying to Heroku is a bit more annoying because it doesn't like to accept your login info.
1. `heroku login`
2. `heroku auth:token`
3. `git push heroku master`
  use the auth token as the password, leave the name blank.


Want to check how often the site has been booted up (ie, a dyno has been created)?
Use `heroku ps`


#### Loading Data into the Database
The site uses fixtures, so add them appropriately into art_fixture_heroku.json file. Ignore the art_fixture and code_fixture files unless doing something explicitly for local server purposes.

The command to load them into the local db is
`manage.py loaddata theactualsite/fixtures/art_fixture_heroku`  
or  
`manage.py loaddata theactualsite/fixtures/code_fixture_heroku`

If you are loading data into the remote db, you're first going to want to push the fixture file to it using
`git push heroku master`

Then, you will use
`heroku run python manage.py loaddata theactualsite/fixtures/art_fixture_heroku`

